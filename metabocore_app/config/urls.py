"""URL configuration for the MetaboCore form viewer prototype."""
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="form_viewer:form_list", permanent=False)),
    path("formatos/", include("form_viewer.urls")),
]
