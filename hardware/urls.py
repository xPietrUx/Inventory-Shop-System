from django.urls import path
from . import views

app_name = "hardware"

urlpatterns = [
    # Hardware
    path("hardware/", views.hardware_list_view, name="hardware_list"),
    path("hardware/add/", views.hardware_add_view, name="hardware_add"),
    path("hardware/<int:pk>/edit/", views.hardware_edit_view, name="hardware_edit"),
    path(
        "hardware/<int:pk>/delete/", views.hardware_delete_view, name="hardware_delete"
    ),
    # History
    path("history/", views.history_list_view, name="history_list"),
    # Projects
    path("project/", views.project_list_view, name="project_list"),
    path("project/add/", views.project_add_view, name="project_add"),
    path("project/<int:pk>/edit/", views.project_edit_view, name="project_edit"),
    path("project/<int:pk>/delete/", views.project_delete_view, name="project_delete"),
]
