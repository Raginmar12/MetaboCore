"""Read-only views for rendering MetaboCore clinical form schemas."""
from __future__ import annotations

import json

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .flow_loaders import get_block_or_404, get_flow_or_404, list_flows
from .flow_renderers import build_block_detail, build_flow_stages, build_flow_timeline
from .loaders import (
    FormViewerError,
    get_form_bundle_or_404,
    list_form_ids,
    load_form_schema,
    load_ui_schema,
    validate_formato_id,
)
from .renderers import build_form_sections, build_print_sections

WARNING_TEXT = (
    "Prototipo de visualización. No introducir datos reales de pacientes. "
    "No guarda información. No declara cumplimiento NOM-004."
)


def _base_context() -> dict[str, str]:
    return {"warning_text": WARNING_TEXT}




@require_GET
def flow_list(request):
    flows = [flow.data for flow in list_flows()]
    return render(
        request,
        "form_viewer/flow_list.html",
        {**_base_context(), "flows": flows},
    )


@require_GET
def flow_detail(request, flow_slug: str):
    flow = get_flow_or_404(flow_slug)
    timeline = build_flow_timeline(flow.data)
    stages = build_flow_stages(flow.data)
    return render(
        request,
        "form_viewer/flow_detail.html",
        {
            **_base_context(),
            "flow": flow.data,
            "timeline": timeline,
            "stages": stages,
            "read_only_note": (
                "Mapa operativo de consulta; no es expediente clínico electrónico."
            ),
        },
    )


@require_GET
def flow_block(request, flow_slug: str, block_slug: str):
    flow, _block = get_block_or_404(flow_slug, block_slug)
    block = build_block_detail(flow.data, block_slug)
    return render(
        request,
        "form_viewer/flow_block.html",
        {
            **_base_context(),
            "flow": flow.data,
            "flow_block": block,
            "read_only_note": (
                "Mapa operativo de consulta; no es expediente clínico electrónico."
            ),
        },
    )


def form_list(request):
    formatos = [{"formato_id": formato_id} for formato_id in list_form_ids()]
    return render(
        request,
        "form_viewer/form_list.html",
        {**_base_context(), "formatos": formatos},
    )


def form_detail(request, formato_id: str):
    bundle = get_form_bundle_or_404(formato_id)
    sections = build_form_sections(bundle.schema, bundle.ui_schema)
    return render(
        request,
        "form_viewer/form_detail.html",
        {
            **_base_context(),
            "formato_id": bundle.formato_id,
            "title": bundle.schema.get("title", bundle.formato_id),
            "description": bundle.schema.get("description", ""),
            "sections": sections,
            "is_example": False,
        },
    )


def form_example(request, formato_id: str):
    bundle = get_form_bundle_or_404(formato_id)
    sections = build_form_sections(bundle.schema, bundle.ui_schema, bundle.example)
    return render(
        request,
        "form_viewer/form_detail.html",
        {
            **_base_context(),
            "formato_id": bundle.formato_id,
            "title": bundle.schema.get("title", bundle.formato_id),
            "description": bundle.schema.get("description", ""),
            "sections": sections,
            "is_example": True,
        },
    )


def _load_print_assets_or_404(formato_id: str):
    try:
        formato_id = validate_formato_id(formato_id)
        schema = load_form_schema(formato_id)
        ui_schema = load_ui_schema(formato_id)
    except FormViewerError as exc:
        raise Http404(str(exc)) from exc
    return formato_id, schema, ui_schema


def _patient_title(schema: dict, formato_id: str) -> str:
    title = schema.get("title", formato_id)
    return title.replace(" MetaboCore", "")


def _render_print_view(request, formato_id: str, variant: str):
    formato_id, schema, ui_schema = _load_print_assets_or_404(formato_id)
    sections = build_print_sections(schema, ui_schema, variant=variant)
    title = _patient_title(schema, formato_id)
    is_patient = variant == "paciente"
    return render(
        request,
        "form_viewer/form_print.html",
        {
            **_base_context(),
            "formato_id": formato_id,
            "schema": schema,
            "ui_schema": ui_schema,
            "sections": sections,
            "is_print_view": True,
            "print_variant": variant,
            "is_patient_print": is_patient,
            "page_title": title if is_patient else f"{title} · Vista imprimible técnica",
            "title": title,
            "heading": "MetaboCare" if is_patient else "MetaboCare / MetaboCore",
            "subheading": (
                "Por favor llene este formato antes de su consulta."
                if is_patient
                else "Vista imprimible técnica"
            ),
            "print_note": (
                ""
                if is_patient
                else (
                    "Formato para uso clínico interno. "
                    "No declara cumplimiento completo NOM-004 por sí mismo."
                )
            ),
            "screen_warning": (
                "Prototipo de visualización. "
                "No introducir datos reales en el visor."
            ),
        },
    )


@require_GET
def form_print_patient(request, formato_id: str):
    return _render_print_view(request, formato_id, "paciente")


@require_GET
def form_print_technical(request, formato_id: str):
    return _render_print_view(request, formato_id, "tecnica")


def _json_context(formato_id: str, document: dict, document_title: str, is_example: bool = False):
    return {
        **_base_context(),
        "formato_id": formato_id,
        "document_title": document_title,
        "json_document": json.dumps(document, ensure_ascii=False, indent=2),
        "is_example": is_example,
    }


def schema_view(request, formato_id: str):
    bundle = get_form_bundle_or_404(formato_id)
    return render(
        request,
        "form_viewer/schema_view.html",
        _json_context(bundle.formato_id, bundle.schema, "JSON Schema"),
    )


def ui_schema_view(request, formato_id: str):
    bundle = get_form_bundle_or_404(formato_id)
    return render(
        request,
        "form_viewer/schema_view.html",
        _json_context(bundle.formato_id, bundle.ui_schema, "UI schema"),
    )


def example_json_view(request, formato_id: str):
    bundle = get_form_bundle_or_404(formato_id)
    return render(
        request,
        "form_viewer/schema_view.html",
        _json_context(
            bundle.formato_id,
            bundle.example,
            "JSON de ejemplo ficticio",
            is_example=True,
        ),
    )
