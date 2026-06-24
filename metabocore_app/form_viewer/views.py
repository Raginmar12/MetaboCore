"""Read-only views for rendering MetaboCore clinical form schemas."""
from __future__ import annotations

import json

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_GET

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


@require_GET
def form_print(request, formato_id: str):
    try:
        formato_id = validate_formato_id(formato_id)
        schema = load_form_schema(formato_id)
        ui_schema = load_ui_schema(formato_id)
    except FormViewerError as exc:
        raise Http404(str(exc)) from exc

    sections = build_print_sections(schema, ui_schema)
    page_title = f"{schema.get('title', formato_id)} · Formato imprimible"
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
            "page_title": page_title,
            "title": schema.get("title", formato_id),
            "description": schema.get("description", ""),
            "print_note": (
                "Formato para uso clínico interno. "
                "No declara cumplimiento completo NOM-004 por sí mismo."
            ),
            "screen_warning": (
                "Prototipo de visualización. "
                "No introducir datos reales en el visor."
            ),
        },
    )


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
