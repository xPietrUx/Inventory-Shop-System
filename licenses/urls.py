# filepath: c:\Users\Piotr\Desktop\Inventory-Shop-System\licenses\urls.py
from django.urls import path
from . import views

app_name = "licenses"

urlpatterns = [
    # URLs for Software model
    path("software/", views.software_list_view, name="software_list"),
    path("software/add/", views.software_add_view, name="software_add"),
    path("software/edit/", views.software_edit_view, name="software_edit"),
    path("software/delete/", views.software_delete_view, name="software_delete"),
    # URLs for License model
    path("license/", views.license_list_view, name="license_list"),
    path("license/add/", views.license_add_view, name="license_add"),
    path("license/edit/", views.license_edit_view, name="license_edit"),
    path("license/delete/", views.license_delete_view, name="license_delete"),
]
