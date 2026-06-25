"""Prepare consultation flow maps for read-only template rendering."""
from __future__ import annotations

from typing import Any

from django.urls import reverse

FORMAT_LINK_LABELS = {
    "preview": "Preview",
    "ejemplo_ficticio": "Ejemplo ficticio",
    "imprimir_paciente": "Imprimir paciente",
    "imprimir_tecnica": "Imprimir técnica",
    "schema": "Schema",
    "ui_schema": "UI schema",
    "json_ejemplo": "JSON ejemplo",
    "documento": "Documento",
}

FORMAT_ROUTE_NAMES = {
    "preview": "form_viewer:form_detail",
    "ejemplo_ficticio": "form_viewer:form_example",
    "imprimir_paciente": "form_viewer:form_print_patient",
    "imprimir_tecnica": "form_viewer:form_print_technical",
    "schema": "form_viewer:schema_view",
    "ui_schema": "form_viewer:ui_schema_view",
    "json_ejemplo": "form_viewer:example_json_view",
}

SCHEMA_LINKS = {
    "preview",
    "ejemplo_ficticio",
    "imprimir_paciente",
    "imprimir_tecnica",
    "schema",
    "ui_schema",
    "json_ejemplo",
}


def _display_format_name(formato_id: str) -> str:
    return formato_id.replace("_", " ").capitalize()


def _format_badge(format_data: dict[str, Any]) -> str:
    if format_data.get("tiene_schema"):
        return "schema"
    estado = format_data.get("estado", "")
    if estado == "futuro":
        return "futuro"
    if estado == "referencia" or format_data.get("tipo") == "referencia":
        return "referencia"
    if format_data.get("tiene_documento"):
        return "documento"
    return "sin_schema"


def build_format_links(format_data: dict[str, Any]) -> list[dict[str, str]]:
    """Build only links that can be resolved for the associated format."""
    formato_id = format_data.get("formato_id", "")
    requested_links = format_data.get("enlaces", [])
    links: list[dict[str, str]] = []

    for link_key in requested_links:
        if link_key in SCHEMA_LINKS:
            if not format_data.get("tiene_schema"):
                continue
            route_name = FORMAT_ROUTE_NAMES[link_key]
            links.append(
                {
                    "key": link_key,
                    "label": FORMAT_LINK_LABELS[link_key],
                    "url": reverse(route_name, args=[formato_id]),
                }
            )
        elif link_key == "documento" and format_data.get("tiene_documento"):
            links.append(
                {
                    "key": link_key,
                    "label": FORMAT_LINK_LABELS[link_key],
                    "url": "",
                }
            )
    return links


def build_format_summary(format_data: dict[str, Any]) -> dict[str, Any]:
    formato_id = str(format_data.get("formato_id", ""))
    return {
        **format_data,
        "nombre": _display_format_name(formato_id),
        "badge": _format_badge(format_data),
        "links": build_format_links(format_data),
    }


def _ordered_blocks(flow: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted(flow.get("bloques", []), key=lambda block: block.get("orden", 0))


def build_flow_timeline(flow: dict[str, Any]) -> list[dict[str, Any]]:
    """Build ordered blocks with safe, template-friendly format summaries."""
    timeline = []
    for block in _ordered_blocks(flow):
        timeline.append(
            {
                **block,
                "formatos_asociados": [
                    build_format_summary(format_data)
                    for format_data in block.get("formatos_asociados", [])
                ],
            }
        )
    return timeline


def _blocks_by_id(flow: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(block.get("bloque_id", "")): block for block in build_flow_timeline(flow)}


def build_flow_stages(flow: dict[str, Any]) -> list[dict[str, Any]]:
    """Build ordered flow stages with associated blocks.

    Flows without `etapas` are returned as one operational stage so older or
    smaller flow maps continue rendering.
    """
    stages = flow.get("etapas", [])
    if not stages:
        return [
            {
                "etapa_id": "flujo_operativo",
                "slug": "flujo-operativo",
                "orden": 1,
                "titulo": "Flujo operativo",
                "descripcion": "Bloques clínico-operativos del flujo.",
                "bloques": build_flow_timeline(flow),
            }
        ]

    block_map = _blocks_by_id(flow)
    rendered_stages = []
    for stage in sorted(stages, key=lambda item: item.get("orden", 0)):
        stage_blocks = [
            block_map[block_id]
            for block_id in stage.get("bloques", [])
            if block_id in block_map
        ]
        rendered_stages.append(
            {
                **stage,
                "bloques": stage_blocks,
            }
        )
    return rendered_stages


def find_stage_for_block(flow: dict[str, Any], block_slug: str) -> dict[str, Any] | None:
    for stage in build_flow_stages(flow):
        for block in stage.get("bloques", []):
            if block.get("slug") == block_slug:
                return {
                    "etapa_id": stage.get("etapa_id", ""),
                    "slug": stage.get("slug", ""),
                    "orden": stage.get("orden", ""),
                    "titulo": stage.get("titulo", ""),
                    "descripcion": stage.get("descripcion", ""),
                }
    return None


def build_block_detail(flow: dict[str, Any], block_slug: str) -> dict[str, Any]:
    """Build one block with previous/next navigation metadata."""
    blocks = build_flow_timeline(flow)
    for index, block in enumerate(blocks):
        if block.get("slug") == block_slug:
            previous_block = blocks[index - 1] if index > 0 else None
            next_block = blocks[index + 1] if index + 1 < len(blocks) else None
            return {
                **block,
                "stage": find_stage_for_block(flow, block_slug),
                "previous_block": previous_block,
                "next_block": next_block,
            }
    raise ValueError(f"No existe el bloque con slug: {block_slug}")
