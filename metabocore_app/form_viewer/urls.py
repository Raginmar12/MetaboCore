"""Routes for the read-only clinical form viewer."""
from django.urls import path

from . import views

app_name = "form_viewer"

urlpatterns = [
    path("", views.form_list, name="form_list"),
    path("<str:formato_id>/", views.form_detail, name="form_detail"),
    path("<str:formato_id>/ejemplo/", views.form_example, name="form_example"),
    path("<str:formato_id>/imprimir/", views.form_print, name="form_print"),
    path("<str:formato_id>/schema/", views.schema_view, name="schema_view"),
    path("<str:formato_id>/ui-schema/", views.ui_schema_view, name="ui_schema_view"),
    path("<str:formato_id>/json-ejemplo/", views.example_json_view, name="example_json_view"),
]
