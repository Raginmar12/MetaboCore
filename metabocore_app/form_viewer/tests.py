"""Tests for the read-only MetaboCore form viewer prototype."""
from __future__ import annotations

from django.apps import apps
from django.test import Client, TestCase
from jsonschema import validate

from .loaders import get_form_bundle, list_form_ids
from .renderers import build_print_sections

WARNING_FRAGMENT = "No introducir datos reales"


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
        sections = build_print_sections(bundle.schema, bundle.ui_schema)
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
            "Motivo breve de consulta",
        )
        self.assertTrue(fields["nombre_completo"]["is_required"])

    def test_print_sections_render_objects_as_subsections(self):
        bundle = get_form_bundle("ficha_inicial")
        sections = build_print_sections(bundle.schema, bundle.ui_schema)
        fields = {
            field["key"]: field
            for section in sections
            for field in section["fields"]
        }
        self.assertEqual(fields["domicilio"]["print_control"], "subsection")
        self.assertGreater(len(fields["domicilio"]["children"]), 0)

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

    def test_form_list_links_to_print_view(self):
        response = self.client.get("/formatos/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Imprimible")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/")

    def test_form_detail_links_to_print_view(self):
        response = self.client.get("/formatos/ficha_inicial/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Imprimible")
        self.assertContains(response, "/formatos/ficha_inicial/imprimir/")

    def test_form_print_responds_200(self):
        response = self.client.get("/formatos/ficha_inicial/imprimir/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Formato imprimible")
        self.assertContains(response, "No introducir datos reales")
        self.assertContains(response, "No declara cumplimiento completo NOM-004")
        self.assertContains(response, "Datos del paciente")
        self.assertContains(response, "Contacto")
        self.assertContains(response, "Datos de la consulta")
        self.assertContains(response, "Motivo de consulta")
        self.assertContains(response, "Nombre completo")
        self.assertContains(response, "Teléfono")
        self.assertContains(response, "Municipio o localidad")
        self.assertContains(response, "Motivo breve de consulta")
        self.assertContains(response, "* Campo recomendado para identificación inicial.")
        self.assertNotContains(response, "Paciente Ficticia MetaboCore")
        self.assertNotContains(response, "Metadatos")
        self.assertNotContains(response, "identidad_paciente")
        self.assertNotContains(response, "contexto_visita_inicial")
        self.assertNotContains(response, "req. técnico")
        self.assertNotContains(response, "requerido visual")
        self.assertNotContains(response, "ui:widget")
        self.assertNotContains(response, "schema")
        self.assertNotContains(response, "JSON")

    def test_form_print_post_is_not_allowed(self):
        response = self.client.post(
            "/formatos/ficha_inicial/imprimir/", {"nombre_completo": "No guardar"}
        )
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
