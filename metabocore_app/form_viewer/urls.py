"""Routes for the read-only clinical form viewer."""
from django.urls import path

from . import views

app_name = "form_viewer"

urlpatterns = [
    path("flujos/", views.flow_list, name="flow_list"),
    path("flujos/<str:flow_slug>/", views.flow_detail, name="flow_detail"),
    path(
        "flujos/<str:flow_slug>/bloque/<str:block_slug>/",
        views.flow_block,
        name="flow_block",
    ),
    path("formatos/", views.form_list, name="form_list"),
    path("formatos/<str:formato_id>/", views.form_detail, name="form_detail"),
    path("formatos/<str:formato_id>/ejemplo/", views.form_example, name="form_example"),
    path("formatos/<str:formato_id>/imprimir/", views.form_print_patient, name="form_print"),
    path(
        "formatos/<str:formato_id>/imprimir/paciente/",
        views.form_print_patient,
        name="form_print_patient",
    ),
    path(
        "formatos/<str:formato_id>/imprimir/tecnica/",
        views.form_print_technical,
        name="form_print_technical",
    ),
    path("formatos/<str:formato_id>/schema/", views.schema_view, name="schema_view"),
    path("formatos/<str:formato_id>/ui-schema/", views.ui_schema_view, name="ui_schema_view"),
    path("formatos/<str:formato_id>/json-ejemplo/", views.example_json_view, name="example_json_view"),
]
