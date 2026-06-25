"""Load consultation flow maps for the read-only viewer.

The loader only reads JSON files from `schemas/flows/`. It does not accept
arbitrary paths, does not persist data and does not load patient records.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from django.conf import settings
from django.http import Http404

from .loaders import SAFE_FORM_ID_RE, list_form_ids

SAFE_FLOW_ID_RE = re.compile(r"^[a-z0-9_]+$")
SAFE_SLUG_RE = re.compile(r"^[a-z0-9-]+$")


class FlowViewerError(Exception):
    """Base error for consultation flow loading problems."""


class UnsafeFlowIdError(FlowViewerError):
    """Raised when a flow id or slug could be used as an unsafe path."""


class FlowAssetNotFoundError(FlowViewerError):
    """Raised when an expected flow asset does not exist."""


@dataclass(frozen=True)
class FlowBundle:
    """Structured consultation flow loaded from schemas/flows."""

    flow_id: str
    slug: str
    data: dict[str, Any]


def _schemas_dir() -> Path:
    return Path(settings.SCHEMAS_DIR).resolve()


def _flows_dir() -> Path:
    return (_schemas_dir() / "flows").resolve()


def validate_flow_id(flow_id: str) -> str:
    """Validate that a flow id cannot escape the flows directory."""
    if not SAFE_FLOW_ID_RE.fullmatch(flow_id):
        raise UnsafeFlowIdError(
            "El flow_id solo puede usar letras minúsculas, números y guion bajo."
        )
    return flow_id


def validate_slug(slug: str) -> str:
    """Validate a public flow or block slug."""
    if not SAFE_SLUG_RE.fullmatch(slug):
        raise UnsafeFlowIdError(
            "El slug solo puede usar letras minúsculas, números y guion medio."
        )
    return slug


def validate_block_slug(block_slug: str) -> str:
    return validate_slug(block_slug)


def _safe_flow_path(filename: str) -> Path:
    base = _flows_dir()
    path = (base / filename).resolve()
    if base not in path.parents:
        raise UnsafeFlowIdError("Ruta fuera de schemas/flows no permitida.")
    return path


def _load_flow_json(flow_id: str) -> dict[str, Any]:
    flow_id = validate_flow_id(flow_id)
    path = _safe_flow_path(f"{flow_id}.flow.json")
    if not path.exists():
        raise FlowAssetNotFoundError(f"No existe el flujo requerido: {path.name}")
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise FlowViewerError(f"El archivo {path.name} debe contener un objeto JSON.")
    return data


def list_flow_ids() -> list[str]:
    """List available flow ids from `schemas/flows/*.flow.json`."""
    flows_dir = _flows_dir()
    if not flows_dir.exists():
        return []
    flow_ids = []
    for path in flows_dir.glob("*.flow.json"):
        flow_id = path.name.removesuffix(".flow.json")
        if SAFE_FLOW_ID_RE.fullmatch(flow_id):
            flow_ids.append(flow_id)
    return sorted(flow_ids)


def _doc_path_for_format(formato_id: str, tipo: str = "formato") -> Path:
    if tipo == "referencia":
        return Path(settings.BASE_DIR).resolve().parent / "docs" / "00_identidad" / f"{formato_id}.md"
    return Path(settings.BASE_DIR).resolve().parent / "docs" / "02_formatos" / f"{formato_id}.md"


def _enrich_format(format_data: dict[str, Any], schema_form_ids: set[str]) -> dict[str, Any]:
    enriched = dict(format_data)
    formato_id = str(enriched.get("formato_id", ""))
    tipo = str(enriched.get("tipo", "formato"))
    has_safe_id = bool(SAFE_FORM_ID_RE.fullmatch(formato_id))
    doc_path = _doc_path_for_format(formato_id, tipo) if has_safe_id else None
    has_schema = has_safe_id and formato_id in schema_form_ids
    has_document = bool(doc_path and doc_path.exists())
    enriched["tiene_schema"] = has_schema
    enriched["tiene_documento"] = has_document
    enriched["documento_path"] = str(doc_path.relative_to(Path(settings.BASE_DIR).resolve().parent)) if has_document and doc_path else ""
    return enriched


def _enrich_flow(data: dict[str, Any]) -> dict[str, Any]:
    schema_form_ids = set(list_form_ids())
    enriched = dict(data)
    blocks = []
    for block in data.get("bloques", []):
        if not isinstance(block, dict):
            continue
        block_copy = dict(block)
        block_copy["formatos_asociados"] = [
            _enrich_format(format_data, schema_form_ids)
            for format_data in block.get("formatos_asociados", [])
            if isinstance(format_data, dict)
        ]
        blocks.append(block_copy)
    enriched["bloques"] = blocks
    return enriched


def load_flow(flow_id: str) -> FlowBundle:
    """Load a flow by internal flow id."""
    flow_id = validate_flow_id(flow_id)
    data = _enrich_flow(_load_flow_json(flow_id))
    loaded_flow_id = data.get("flow_id")
    slug = data.get("slug")
    if loaded_flow_id != flow_id:
        raise FlowViewerError("El flow_id interno no coincide con el nombre del archivo.")
    if not isinstance(slug, str):
        raise FlowViewerError("El flujo debe declarar slug.")
    validate_slug(slug)
    return FlowBundle(flow_id=flow_id, slug=slug, data=data)


def list_flows() -> list[FlowBundle]:
    """Load all available flows."""
    return [load_flow(flow_id) for flow_id in list_flow_ids()]


def load_flow_by_slug(slug: str) -> FlowBundle:
    """Load a flow by public URL slug."""
    slug = validate_slug(slug)
    for flow in list_flows():
        if flow.slug == slug:
            return flow
    raise FlowAssetNotFoundError(f"No existe el flujo con slug: {slug}")


def get_block(flow_slug: str, block_slug: str) -> tuple[FlowBundle, dict[str, Any]]:
    """Load a block by public flow and block slugs."""
    flow = load_flow_by_slug(validate_slug(flow_slug))
    block_slug = validate_block_slug(block_slug)
    for block in flow.data.get("bloques", []):
        if block.get("slug") == block_slug:
            return flow, block
    raise FlowAssetNotFoundError(f"No existe el bloque con slug: {block_slug}")


def get_flow_or_404(flow_slug: str) -> FlowBundle:
    try:
        return load_flow_by_slug(flow_slug)
    except FlowViewerError as exc:
        raise Http404(str(exc)) from exc


def get_block_or_404(flow_slug: str, block_slug: str) -> tuple[FlowBundle, dict[str, Any]]:
    try:
        return get_block(flow_slug, block_slug)
    except FlowViewerError as exc:
        raise Http404(str(exc)) from exc
