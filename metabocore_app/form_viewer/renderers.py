"""Transform JSON Schema + UI schema into template-friendly structures."""
from __future__ import annotations

from typing import Any


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
                children = _nested_fields(field_schema, value if isinstance(value, dict) else None)

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
                "hidden": bool(section_ui.get("ui:oculto") or section_ui.get("ui:widget") == "hidden"),
                "fields": section_fields,
            }
        )

    return sections


def _is_hidden_field(field_ui: dict[str, Any]) -> bool:
    widget = field_ui.get("ui:widget", "text")
    return bool(field_ui.get("ui:oculto") or widget == "hidden")


def _humanize_field_label(key: str) -> str:
    return humanize_key(key)


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
                "label": _humanize_field_label(child_key),
                "print_control": _print_control_for_field(child_schema, child_ui),
                "required": child_key in required,
                "required_visual": bool(child_ui.get("ui:requerido_visual")),
                "help": child_ui.get("ui:ayuda", child_schema.get("description", "")),
                "options": child_schema.get("enum", []),
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
                    "label": _humanize_field_label(field_key),
                    "print_control": print_control,
                    "required": field_key in section_required,
                    "required_visual": bool(field_ui.get("ui:requerido_visual")),
                    "help": field_ui.get("ui:ayuda", field_schema.get("description", "")),
                    "options": field_schema.get("enum", []),
                    "children": _build_print_children(field_schema, field_ui)
                    if print_control == "subsection"
                    else [],
                    "optional": field_key not in section_required,
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
                "fields": section_fields,
            }
        )

    return sections
