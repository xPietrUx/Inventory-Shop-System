from django.urls import path
from . import views

app_name = "hardware"

urlpatterns = [
    # Hardware paths
    path("hardware/", views.hardware_list_view, name="hardware_list"),
    # History paths
    path("history/", views.hardware_history_list_view, name="hardware_history_list"),
    # Project paths
    path("project/", views.project_list_view, name="project_list"),
]
