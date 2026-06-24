"""Load clinical form schemas for the read-only viewer.

The loader only reads JSON files from the repository `schemas/` directory. It does
not accept arbitrary paths and does not read or persist patient data.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from django.conf import settings
from django.http import Http404

SAFE_FORM_ID_RE = re.compile(r"^[a-z0-9_]+$")


class FormViewerError(Exception):
    """Base error for form viewer loading problems."""


class UnsafeFormIdError(FormViewerError):
    """Raised when a form id could be used as an unsafe path."""


class FormAssetNotFoundError(FormViewerError):
    """Raised when an expected schema asset does not exist."""


@dataclass(frozen=True)
class FormBundle:
    """All JSON assets needed to render a clinical form."""

    formato_id: str
    schema: dict[str, Any]
    ui_schema: dict[str, Any]
    example: dict[str, Any]


def _schemas_dir() -> Path:
    return Path(settings.SCHEMAS_DIR).resolve()


def validate_formato_id(formato_id: str) -> str:
    """Validate that a form id cannot escape the schemas directory."""
    if not SAFE_FORM_ID_RE.fullmatch(formato_id):
        raise UnsafeFormIdError(
            "El formato_id solo puede usar letras minúsculas, números y guion bajo."
        )
    return formato_id


def _safe_json_path(folder: str, filename: str) -> Path:
    base = (_schemas_dir() / folder).resolve()
    path = (base / filename).resolve()
    if base not in path.parents:
        raise UnsafeFormIdError("Ruta fuera de schemas no permitida.")
    return path


def _load_json(folder: str, filename: str) -> dict[str, Any]:
    path = _safe_json_path(folder, filename)
    if not path.exists():
        raise FormAssetNotFoundError(f"No existe el archivo requerido: {path.name}")
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise FormViewerError(f"El archivo {path.name} debe contener un objeto JSON.")
    return data


def list_form_ids() -> list[str]:
    """List available form ids from `schemas/forms/*.schema.json`."""
    forms_dir = _schemas_dir() / "forms"
    if not forms_dir.exists():
        return []
    form_ids = []
    for path in forms_dir.glob("*.schema.json"):
        formato_id = path.name.removesuffix(".schema.json")
        if SAFE_FORM_ID_RE.fullmatch(formato_id):
            form_ids.append(formato_id)
    return sorted(form_ids)


def load_form_schema(formato_id: str) -> dict[str, Any]:
    formato_id = validate_formato_id(formato_id)
    return _load_json("forms", f"{formato_id}.schema.json")


def load_ui_schema(formato_id: str) -> dict[str, Any]:
    formato_id = validate_formato_id(formato_id)
    return _load_json("ui", f"{formato_id}.ui.json")


def load_example(formato_id: str) -> dict[str, Any]:
    formato_id = validate_formato_id(formato_id)
    return _load_json("examples", f"{formato_id}.example.json")


def get_form_bundle(formato_id: str) -> FormBundle:
    """Load schema, UI schema and fictitious example for a form."""
    formato_id = validate_formato_id(formato_id)
    return FormBundle(
        formato_id=formato_id,
        schema=load_form_schema(formato_id),
        ui_schema=load_ui_schema(formato_id),
        example=load_example(formato_id),
    )


def get_form_bundle_or_404(formato_id: str) -> FormBundle:
    try:
        return get_form_bundle(formato_id)
    except FormViewerError as exc:
        raise Http404(str(exc)) from exc
