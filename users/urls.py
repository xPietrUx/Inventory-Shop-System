from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = "users"

urlpatterns = [
    # users paths
    path("users/", views.users_list_view, name="users_list"),
    path("users/add/", views.users_add_view, name="users_add"),
    path("users/<int:pk>/edit/", views.users_edit_view, name="users_edit"),
    path("users/<int:pk>/delete/", views.users_delete_view, name="users_delete"),
    # roles paths
    path("roles/", views.roles_list_view, name="roles_list"),
    path("roles/add/", views.roles_add_view, name="roles_add"),
    path("roles/<int:pk>/edit/", views.roles_edit_view, name="roles_edit"),
    path("roles/<int:pk>/delete/", views.roles_delete_view, name="roles_delete"),
    # redirect from / to users/
    path("", RedirectView.as_view(url="users/", permanent=False)),
]
