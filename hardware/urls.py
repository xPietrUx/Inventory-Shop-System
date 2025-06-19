from django.urls import path

from .views import (
    HardwareListView,
    HardwareAddView,
    HardwareEditView,
    HardwareDeleteView,
    HardwareHistoryListView,
    HardwareHistoryEditView,
    HardwareHistoryDeleteView,
    ProjectListView,
    ProjectAddView,
    ProjectEditView,
    ProjectDeleteView,
)

app_name = "hardware"
urlpatterns = [
    # Hardware
    path("hardware/", HardwareListView.as_view(), name="hardware_list"),
    path("hardware/add/", HardwareAddView.as_view(), name="hardware_add"),
    path("hardware/<int:pk>/edit/", HardwareEditView.as_view(), name="hardware_edit"),
    path(
        "hardware/<int:pk>/delete/",
        HardwareDeleteView.as_view(),
        name="hardware_delete",
    ),
    # Hardware History
    path(
        "hardware/history/<int:hardware_id>/",
        HardwareHistoryListView.as_view(),
        name="hardware_history",
    ),
    path(
        "hardware/history/edit/<int:pk>/",
        HardwareHistoryEditView.as_view(),
        name="hardware_history_edit",
    ),
    path(
        "hardware/history/delete/<int:pk>/",
        HardwareHistoryDeleteView.as_view(),
        name="hardware_history_delete",
    ),
    # Projects
    path("projects/", ProjectListView.as_view(), name="project_list"),
    path("projects/add/", ProjectAddView.as_view(), name="project_add"),
    path("projects/edit/<int:pk>/", ProjectEditView.as_view(), name="project_edit"),
    path("projects/delete/<int:pk>/", ProjectDeleteView.as_view(), name="project_delete"),
]
