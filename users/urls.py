from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = "users"

urlpatterns = [
    path("users/", views.users_list_view, name="users_list"),
    path("users/add/", views.users_add_view, name="users_add"),
    path("users/<int:pk>/edit/", views.users_edit_view, name="users_edit"),
    path("", RedirectView.as_view(url="users/", permanent=False)),
]
