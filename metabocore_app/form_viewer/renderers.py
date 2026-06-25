"""Transform JSON Schema + UI schema into template-friendly structures."""
from __future__ import annotations

from typing import Any


PRINT_SECTION_TITLES = {
    "identidad_paciente": "Datos del paciente",
    "contacto": "Contacto",
    "contexto_administrativo": "Datos de la consulta",
    "contexto_visita_inicial": "Motivo de consulta",
}

PRINT_FIELD_LABELS = {
    "nombre_completo": "Nombre completo",
    "nombre_preferido": "Nombre preferido",
    "fecha_nacimiento": "Fecha de nacimiento",
    "sexo_registrado": "Sexo",
    "genero": "Género",
    "telefono_principal": "Teléfono",
    "telefono_alterno": "Teléfono alterno",
    "correo_electronico": "Correo electrónico",
    "municipio_o_localidad": "Municipio o localidad",
    "preferencia_comunicacion": "Preferencia de comunicación",
    "fecha_primera_consulta": "Fecha de primera consulta",
    "medico_responsable": "Médico responsable",
    "motivo_breve_consulta": "Motivo breve de consulta",
    "preocupacion_inicial": "Preocupación inicial",
    "ocupacion_o_actividad_principal": "Ocupación o actividad principal",
    "contacto_emergencia": "Contacto de emergencia",
    "referencia_aviso_privacidad": "Aviso de privacidad",
    "consentimiento_verbal_flujo_consulta": (
        "Consentimiento verbal para flujo de consulta"
    ),
    "observaciones": "Observaciones",
    "codigo_postal": "Código postal",
    "numero_exterior": "Número exterior",
    "numero_interior": "Número interior",
}

PRINT_OPTION_LABELS = {
    "correo_electronico": "Correo electrónico",
    "no_especificado": "No especificado",
}


def humanize_key(key: str) -> str:
    """Convert a snake_case technical key into a readable Spanish label."""
    return key.replace("_", " ").capitalize()


def _field_value(example: dict[str, Any] | None, section_key: str, field_key: str) -> Any:
    if not example:
        return None
    section_value = example.get(section_key)
    if isinstance(section_value, dict):
        return section_value.get(field_key)
    return None


def _nested_fields(
    field_schema: dict[str, Any],
    value: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    properties = field_schema.get("properties", {})
    required = set(field_schema.get("required", []))
    fields = []
    for key, schema in properties.items():
        fields.append(
            {
                "key": key,
                "label": humanize_key(key),
                "type": schema.get("type", "string"),
                "required": key in required,
                "value": value.get(key) if isinstance(value, dict) else None,
                "options": schema.get("enum", []),
                "description": schema.get("description", ""),
            }
        )
    return fields


def build_form_sections(
    schema: dict[str, Any],
    ui_schema: dict[str, Any],
    example: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Build sections for template rendering without generating raw HTML."""
    schema_properties = schema.get("properties", {})
    root_required = set(schema.get("required", []))
    section_order = ui_schema.get("ui:orden_secciones", list(schema_properties.keys()))
    sections: list[dict[str, Any]] = []

    for section_key in section_order:
        section_schema = schema_properties.get(section_key, {})
        section_ui = ui_schema.get(section_key, {})
        section_properties = section_schema.get("properties", {})
        section_required = set(section_schema.get("required", []))
        field_order = section_ui.get("ui:orden_campos", list(section_properties.keys()))
        section_fields = []

        for field_key in field_order:
            field_schema = section_properties.get(field_key, {})
            field_ui = section_ui.get(field_key, {})
            value = _field_value(example, section_key, field_key)
            widget = field_ui.get("ui:widget", "text")
            is_hidden = bool(field_ui.get("ui:oculto") or widget == "hidden")
            field_type = field_schema.get("type", "string")
            children = []
            if field_type == "object":
                children = _nested_fields(
                    field_schema, value if isinstance(value, dict) else None
                )

            section_fields.append(
                {
                    "key": field_key,
                    "label": humanize_key(field_key),
                    "type": field_type,
                    "widget": widget,
                    "required": field_key in section_required,
                    "required_visual": bool(field_ui.get("ui:requerido_visual")),
                    "help": field_ui.get("ui:ayuda", field_schema.get("description", "")),
                    "value": value,
                    "options": field_schema.get("enum", []),
                    "collapsed": bool(field_ui.get("ui:colapsado")),
                    "hidden": is_hidden,
                    "readonly": bool(field_ui.get("ui:solo_lectura")),
                    "children": children,
                }
            )

        sections.append(
            {
                "key": section_key,
                "title": section_ui.get("ui:titulo", humanize_key(section_key)),
                "description": section_ui.get(
                    "ui:descripcion", section_schema.get("description", "")
                ),
                "required": section_key in root_required,
                "hidden": bool(
                    section_ui.get("ui:oculto")
                    or section_ui.get("ui:widget") == "hidden"
                ),
                "fields": section_fields,
            }
        )

    return sections


def _is_hidden_field(field_ui: dict[str, Any]) -> bool:
    widget = field_ui.get("ui:widget", "text")
    return bool(field_ui.get("ui:oculto") or widget == "hidden")


def _humanize_print_text(value: str) -> str:
    return value.replace("_", " ").capitalize()


def _humanize_field_label(key: str) -> str:
    return PRINT_FIELD_LABELS.get(key, _humanize_print_text(key))


def _humanize_section_title(key: str, section_ui: dict[str, Any]) -> str:
    return PRINT_SECTION_TITLES.get(
        key, section_ui.get("ui:titulo", _humanize_print_text(key))
    )


def _humanize_option(option: Any) -> str:
    option_text = str(option)
    return PRINT_OPTION_LABELS.get(option_text, _humanize_print_text(option_text))


def _print_control_for_field(field_schema: dict[str, Any], field_ui: dict[str, Any]) -> str:
    widget = field_ui.get("ui:widget", "text")
    field_type = field_schema.get("type", "string")
    if field_type == "object" or widget.startswith("object/"):
        return "subsection"
    if field_schema.get("enum") or widget == "select":
        return "checkbox_group"
    if field_type == "boolean" or widget == "checkbox":
        return "checkbox"
    if widget == "textarea":
        return "multiline"
    return "line"


def _build_print_children(
    field_schema: dict[str, Any],
    field_ui: dict[str, Any],
) -> list[dict[str, Any]]:
    properties = field_schema.get("properties", {})
    required = set(field_schema.get("required", []))
    field_order = field_ui.get("ui:orden_campos", list(properties.keys()))
    children = []

    for child_key in field_order:
        child_schema = properties.get(child_key, {})
        child_ui = field_ui.get(child_key, {})
        if _is_hidden_field(child_ui):
            continue
        children.append(
            {
                "key": child_key,
                "display_label": _humanize_field_label(child_key),
                "print_control": _print_control_for_field(child_schema, child_ui),
                "is_required": bool(
                    child_key in required or child_ui.get("ui:requerido_visual")
                ),
                "help": child_ui.get("ui:ayuda", child_schema.get("description", "")),
                "options": [
                    {"value": option, "label": _humanize_option(option)}
                    for option in child_schema.get("enum", [])
                ],
                "children": _build_print_children(child_schema, child_ui)
                if child_schema.get("type") == "object"
                else [],
                "optional": child_key not in required,
            }
        )
    return children


def build_print_sections(
    schema: dict[str, Any],
    ui_schema: dict[str, Any],
) -> list[dict[str, Any]]:
    """Build sections for print rendering from JSON Schema + UI schema only."""
    schema_properties = schema.get("properties", {})
    root_required = set(schema.get("required", []))
    section_order = ui_schema.get("ui:orden_secciones", list(schema_properties.keys()))
    sections: list[dict[str, Any]] = []

    for section_key in section_order:
        section_schema = schema_properties.get(section_key, {})
        section_ui = ui_schema.get(section_key, {})
        section_is_hidden = bool(
            section_key == "metadatos"
            or section_ui.get("ui:oculto")
            or section_ui.get("ui:widget") == "hidden"
        )
        if section_is_hidden:
            continue

        section_properties = section_schema.get("properties", {})
        section_required = set(section_schema.get("required", []))
        field_order = section_ui.get("ui:orden_campos", list(section_properties.keys()))
        section_fields = []

        for field_key in field_order:
            field_schema = section_properties.get(field_key, {})
            field_ui = section_ui.get(field_key, {})
            if _is_hidden_field(field_ui):
                continue

            print_control = _print_control_for_field(field_schema, field_ui)
            section_fields.append(
                {
                    "key": field_key,
                    "display_label": _humanize_field_label(field_key),
                    "print_control": print_control,
                    "is_required": bool(
                        field_key in section_required
                        or field_ui.get("ui:requerido_visual")
                    ),
                    "help": field_ui.get("ui:ayuda", field_schema.get("description", "")),
                    "options": [
                        {"value": option, "label": _humanize_option(option)}
                        for option in field_schema.get("enum", [])
                    ],
                    "children": _build_print_children(field_schema, field_ui)
                    if print_control == "subsection"
                    else [],
                    "optional": field_key not in section_required,
                }
            )

        sections.append(
            {
                "key": section_key,
                "display_title": _humanize_section_title(section_key, section_ui),
                "description": section_ui.get(
                    "ui:descripcion", section_schema.get("description", "")
                ),
                "is_required": section_key in root_required,
                "has_required_fields": any(
                    field["is_required"] for field in section_fields
                ),
                "fields": section_fields,
            }
        )

    return sections
