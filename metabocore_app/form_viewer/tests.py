"""Tests for the read-only MetaboCore form viewer prototype."""
from __future__ import annotations

from django.apps import apps
from django.test import Client, TestCase
from jsonschema import validate

from .flow_loaders import (
    FlowViewerError,
    list_flow_ids,
    load_flow,
    load_flow_by_slug,
    validate_flow_id,
    validate_slug,
)
from .loaders import get_form_bundle, list_form_ids
from .renderers import build_print_sections

WARNING_FRAGMENT = "No introducir datos reales"




class FlowViewerLoaderTests(TestCase):
    def test_list_flow_ids_includes_initial_flows(self):
        self.assertIn("primera_consulta", list_flow_ids())
        self.assertIn("seguimiento", list_flow_ids())

    def test_load_primera_consulta_flow(self):
        flow = load_flow("primera_consulta")
        self.assertEqual(flow.data["titulo"], "Primera consulta MetaboCare")
        self.assertEqual(len(flow.data["bloques"]), 12)
        self.assertEqual(flow.slug, "primera-consulta")
        self.assertIn("etapas", flow.data)

    def test_primera_consulta_flow_has_expected_stages(self):
        flow = load_flow("primera_consulta")
        stage_ids = [stage["etapa_id"] for stage in flow.data["etapas"]]
        self.assertEqual(
            stage_ids,
            [
                "datos_iniciales",
                "conexion_clinica",
                "historial_clinico_y_antecedentes",
                "medicion_objetiva",
                "integracion_clinica",
                "plan_y_continuidad",
            ],
        )

    def test_seguimiento_flow_matches_declared_ten_step_map(self):
        flow = load_flow("seguimiento")
        block_ids = [block["bloque_id"] for block in flow.data["bloques"]]
        self.assertEqual(
            block_ids,
            [
                "recepcion_breve",
                "revision_objetivo_previo",
                "revision_peso_cintura_sintomas_mediciones",
                "revision_adherencia",
                "revision_efectos_adversos",
                "revision_barreras",
                "ajuste_plan",
                "nuevas_metas",
                "proxima_cita",
                "datos_nota_evolucion_nom",
            ],
        )

    def test_seguimiento_stages_reference_all_and_only_existing_blocks(self):
        flow = load_flow("seguimiento")
        block_ids = {block["bloque_id"] for block in flow.data["bloques"]}
        stage_block_ids = [
            block_id
            for stage in flow.data["etapas"]
            for block_id in stage["bloques"]
        ]
        self.assertEqual(set(stage_block_ids), block_ids)
        self.assertEqual(len(stage_block_ids), len(block_ids))

    def test_antecedentes_before_habitos(self):
        flow = load_flow("primera_consulta")
        blocks = {block["bloque_id"]: block for block in flow.data["bloques"]}
        antecedentes = blocks["antecedentes_clinicos_relevantes_y_seguridad"]
        habitos = blocks["habitos_actuales"]
        self.assertEqual(antecedentes["orden"], 7)
        self.assertEqual(habitos["orden"], 8)
        self.assertLess(antecedentes["orden"], habitos["orden"])
        self.assertEqual(
            antecedentes["titulo"],
            "Antecedentes clínicos relevantes y seguridad",
        )

    def test_load_flow_by_slug(self):
        flow = load_flow_by_slug("primera-consulta")
        self.assertEqual(flow.flow_id, "primera_consulta")

    def test_unsafe_flow_id_fails(self):
        with self.assertRaises(FlowViewerError):
            validate_flow_id("../primera_consulta")

    def test_unsafe_slug_fails(self):
        with self.assertRaises(FlowViewerError):
            validate_slug("../primera-consulta")

    def test_bienvenida_links_to_ficha_inicial(self):
        flow = load_flow("primera_consulta")
        block = next(
            block
            for block in flow.data["bloques"]
            if block["slug"] == "bienvenida-y-encuadre"
        )
        formatos = block["formatos_asociados"]
        self.assertEqual(formatos[0]["formato_id"], "ficha_inicial")
        self.assertTrue(formatos[0]["tiene_schema"])

class FormViewerLoaderTests(TestCase):
    def test_list_form_ids_includes_ficha_inicial(self):
        self.assertIn("ficha_inicial", list_form_ids())

    def test_load_ficha_inicial_bundle(self):
        bundle = get_form_bundle("ficha_inicial")
        self.assertEqual(bundle.schema["properties"]["formato_id"]["const"], "ficha_inicial")
        self.assertEqual(bundle.ui_schema["ui:formato"], "ficha_inicial")
        self.assertTrue(bundle.example["metadatos"]["ejemplo_es_ficticio"])

    def test_example_validates_against_schema(self):
        bundle = get_form_bundle("ficha_inicial")
        validate(instance=bundle.example, schema=bundle.schema)

    def test_ui_schema_has_no_first_level_orphan_fields(self):
        bundle = get_form_bundle("ficha_inicial")
        schema_properties = bundle.schema["properties"]
        for section_key in bundle.ui_schema["ui:orden_secciones"]:
            self.assertIn(section_key, schema_properties)
            section_schema_properties = schema_properties[section_key].get("properties", {})
            for field_key in bundle.ui_schema[section_key].get("ui:orden_campos", []):
                self.assertIn(field_key, section_schema_properties)

    def test_print_sections_omit_metadata(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema)
        self.assertNotIn("metadatos", [section["key"] for section in sections])

    def test_print_sections_convert_controls(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema, variant="tecnica")
        fields = {
            field["key"]: field
            for section in sections
            for field in section["fields"]
        }
        self.assertEqual(fields["sexo_registrado"]["print_control"], "checkbox_group")
        self.assertEqual(
            fields["consentimiento_verbal_flujo_consulta"]["print_control"],
            "checkbox",
        )
        self.assertEqual(fields["motivo_breve_consulta"]["print_control"], "multiline")


    def test_print_sections_use_human_labels(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema)
        self.assertEqual(
            [section["display_title"] for section in sections],
            [
                "Datos del paciente",
                "Contacto",
                "Datos de la consulta",
                "Motivo de consulta",
            ],
        )
        fields = {
            field["key"]: field
            for section in sections
            for field in section["fields"]
        }
        self.assertEqual(fields["telefono_principal"]["display_label"], "Teléfono")
        self.assertEqual(
            fields["motivo_breve_consulta"]["display_label"],
            "Motivo de consulta",
        )
        self.assertTrue(fields["nombre_completo"]["is_required"])

    def test_print_sections_render_objects_as_subsections(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema, variant="tecnica")
        fields = {
            field["key"]: field
            for section in sections
            for field in section["fields"]
        }
        self.assertEqual(fields["domicilio"]["print_control"], "subsection")
        self.assertGreater(len(fields["domicilio"]["children"]), 0)


    def test_patient_print_sections_omit_internal_fields(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema)
        fields = {
            field["key"]: field
            for section in sections
            for field in section["fields"]
        }
        self.assertNotIn("medico_responsable", fields)
        self.assertNotIn("establecimiento", fields)
        self.assertNotIn("domicilio", fields)
        self.assertNotIn("contacto_emergencia", fields)
        self.assertEqual(
            fields["nombre_preferido"]["display_label"],
            "¿Cómo prefiere que le llamemos?",
        )
        self.assertEqual(
            fields["preferencia_comunicacion"]["display_label"],
            "¿Cómo prefiere que le contactemos?",
        )

    def test_technical_print_sections_keep_internal_fields(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema, variant="tecnica")
        fields = {
            field["key"]: field
            for section in sections
            for field in section["fields"]
        }
        self.assertIn("medico_responsable", fields)
        self.assertIn("establecimiento", fields)

    def test_no_clinical_models_defined(self):
        form_viewer_models = list(apps.get_app_config("form_viewer").get_models())
        self.assertEqual(form_viewer_models, [])


class FormViewerRouteTests(TestCase):
    def setUp(self):
        self.client = Client()

    def assert_warning_present(self, response):
        self.assertContains(response, WARNING_FRAGMENT)

    def test_form_list_responds_200(self):
        response = self.client.get("/formatos/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ficha_inicial")
        self.assert_warning_present(response)

    def test_form_detail_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ficha inicial MetaboCore")
        self.assert_warning_present(response)

    def test_form_example_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/ejemplo/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ejemplo ficticio")
        self.assert_warning_present(response)

    def test_form_list_links_to_print_views(self):
        response = self.client.get("/formatos/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Imprimir paciente")
        self.assertContains(response, "Imprimir técnica")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/paciente/")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/tecnica/")

    def test_form_detail_links_to_print_views(self):
        response = self.client.get("/formatos/ficha_inicial/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Imprimir paciente")
        self.assertContains(response, "Imprimir técnica")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/paciente/")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/tecnica/")

    def assert_patient_print_response(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ficha inicial")
        self.assertContains(response, "Por favor llene este formato antes de su consulta")
        self.assertContains(response, "Datos del paciente")
        self.assertContains(response, "Contacto")
        self.assertContains(response, "Motivo de consulta")
        self.assertContains(response, "Nombre completo")
        self.assertContains(response, "Teléfono")
        self.assertContains(response, "Municipio o localidad")
        self.assertContains(response, "¿Cómo prefiere que le llamemos?")
        self.assertContains(response, "¿Cómo prefiere que le contactemos?")
        self.assertNotContains(response, "MetaboCore")
        self.assertNotContains(response, "No declara cumplimiento completo NOM-004")
        self.assertNotContains(response, "sistema futuro")
        self.assertNotContains(response, "configuración futura")
        self.assertNotContains(response, "documentos clínicos posteriores")
        self.assertNotContains(response, "referencia futura")
        self.assertNotContains(response, "Médico responsable")
        self.assertNotContains(response, "medico_responsable")
        self.assertNotContains(response, "id_expediente_interno")
        self.assertNotContains(response, "Establecimiento")
        self.assertNotContains(response, "establecimiento")
        self.assertNotContains(response, "aviso de privacidad")
        self.assertNotContains(response, "consentimiento verbal")
        self.assertNotContains(response, "Metadatos")
        self.assertNotContains(response, "formato_id")
        self.assertNotContains(response, "schema")
        self.assertNotContains(response, "JSON")
        self.assertNotContains(response, "required")
        self.assertNotContains(response, "ui:widget")
        self.assertNotContains(response, "Paciente Ficticia MetaboCore")
        self.assertNotContains(response, "000-000-0000")

    def test_form_print_default_responds_as_patient_view(self):
        response = self.client.get("/formatos/ficha_inicial/imprimir/")
        self.assertContains(response, "print-variant-paciente")
        self.assert_patient_print_response(response)

    def test_form_print_patient_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/imprimir/paciente/")
        self.assertContains(response, "print-variant-paciente")
        self.assert_patient_print_response(response)

    def test_form_print_technical_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/imprimir/tecnica/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vista imprimible técnica")
        self.assertContains(response, "MetaboCare / MetaboCore")
        self.assertContains(response, "No declara cumplimiento completo NOM-004")
        self.assertContains(response, "Médico responsable")
        self.assertContains(response, "Establecimiento")
        self.assertNotContains(response, "Paciente Ficticia MetaboCore")
        self.assertNotContains(response, "000-000-0000")
        self.assertNotContains(response, "JSON")

    def test_form_print_post_is_not_allowed(self):
        for path in (
            "/formatos/ficha_inicial/imprimir/",
            "/formatos/ficha_inicial/imprimir/paciente/",
            "/formatos/ficha_inicial/imprimir/tecnica/",
        ):
            response = self.client.post(path, {"nombre_completo": "No guardar"})
            self.assertEqual(response.status_code, 405)

    def test_flow_list_responds_200(self):
        response = self.client.get("/flujos/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Flujos de consulta")
        self.assertContains(response, "Primera consulta MetaboCare")
        self.assertContains(response, "Seguimiento MetaboCare")
        self.assert_warning_present(response)

    def test_flow_detail_responds_200(self):
        response = self.client.get("/flujos/primera-consulta/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Primera consulta MetaboCare")
        self.assertContains(response, "Datos iniciales")
        self.assertContains(response, "Conexión clínica")
        self.assertContains(response, "Historial clínico y antecedentes")
        self.assertContains(response, "Medición objetiva")
        self.assertContains(response, "Integración clínica")
        self.assertContains(response, "Plan y continuidad")
        self.assertContains(response, "Bienvenida y encuadre")
        self.assertContains(response, "Antecedentes clínicos relevantes y seguridad")
        self.assertContains(response, "Hábitos actuales")
        self.assertContains(response, "Ficha inicial")
        self.assertContains(response, "Mapa operativo")
        self.assertNotContains(response, "Guardar")
        self.assertNotContains(response, "<input")
        self.assertNotContains(response, "completado")
        self.assert_warning_present(response)

    def test_flow_block_responds_200_and_links_to_ficha_inicial_views(self):
        response = self.client.get(
            "/flujos/primera-consulta/bloque/bienvenida-y-encuadre/"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenida y encuadre")
        self.assertContains(response, "Ficha inicial")
        self.assertContains(response, "/formatos/ficha_inicial/")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/paciente/")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/tecnica/")
        self.assertContains(response, "/formatos/ficha_inicial/schema/")
        self.assertContains(response, "/formatos/ficha_inicial/ui-schema/")
        self.assertContains(response, "/formatos/ficha_inicial/json-ejemplo/")
        self.assertNotContains(response, "Guardar")
        self.assertNotContains(response, "<input")
        self.assertNotContains(response, "completado")


    def test_new_antecedentes_and_habitos_block_routes_respond_200(self):
        antecedentes_response = self.client.get(
            "/flujos/primera-consulta/bloque/antecedentes-clinicos-relevantes-y-seguridad/"
        )
        self.assertEqual(antecedentes_response.status_code, 200)
        self.assertContains(
            antecedentes_response,
            "Antecedentes clínicos relevantes y seguridad",
        )
        self.assertContains(
            antecedentes_response,
            "Etapa: Historial clínico y antecedentes",
        )

        habitos_response = self.client.get(
            "/flujos/primera-consulta/bloque/habitos-actuales/"
        )
        self.assertEqual(habitos_response.status_code, 200)
        self.assertContains(habitos_response, "Hábitos actuales")

    def test_flow_post_is_not_allowed(self):
        for path in (
            "/flujos/",
            "/flujos/primera-consulta/",
            "/flujos/primera-consulta/bloque/bienvenida-y-encuadre/",
        ):
            response = self.client.post(path, {"dato": "No guardar"})
            self.assertEqual(response.status_code, 405)

    def test_schema_view_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/schema/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JSON Schema")
        self.assert_warning_present(response)

    def test_ui_schema_view_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/ui-schema/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "UI schema")
        self.assert_warning_present(response)

    def test_example_json_view_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/json-ejemplo/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "JSON de ejemplo ficticio")
        self.assert_warning_present(response)
