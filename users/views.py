from django.shortcuts import render, redirect, get_object_or_404
from .models import Users, Roles
from django import forms


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            "name",
            "surname",
            "position",
            "id_role",
            "email",
            "username",
            "password",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "First Name"},
            ),
            "surname": forms.TextInput(
                attrs={"placeholder": "Last Name"},
            ),
            "position": forms.TextInput(
                attrs={"placeholder": "Position"},
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "E-mail"},
            ),
            "username": forms.TextInput(
                attrs={"placeholder": "Username"},
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Password"},
            ),
        }


class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = [
            "role_name",
            "description",
        ]
        widgets = {
            "role_name": forms.TextInput(attrs={"placeholder": "Name"}),
            "description": forms.TextInput(attrs={"placeholder": "Description"}),
        }


# users views
def users_list_view(request):
    users = Users.objects.all()
    active_nav = "users"
    active_page_title = "Users"

    return render(
        request,
        "users/users_list.html",
        {
            "users": users,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def users_add_view(request):
    active_nav = "users"
    active_page_title = "Users"

    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:users_list")
    else:
        form = UsersForm()

    return render(
        request,
        "users/users/users_add.html",
        {
            "form": form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def users_edit_view(request, pk):
    user = get_object_or_404(Users, pk=pk)
    active_nav = "users"
    active_page_title = f"Edit User: {user.username}"

    if request.method == "POST":
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users:users_list")

    else:
        form = UsersForm(instance=user)

    return render(
        request,
        "users/users/users_edit.html",
        {
            "form": form,
            "user": user,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def users_delete_view(request, pk):
    user = get_object_or_404(Users, pk=pk)
    active_nav = "users"
    active_page_title = f"Delete User: {user.username}"

    if request.method == "POST":
        user.delete()
        return redirect("users:users_list")

    return render(
        request,
        "users/users/users_delete.html",
        {
            "user": user,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


# roles views
def roles_list_view(request):
    roles = Roles.objects.all()
    active_nav = "users"

    return render(
        request,
        "users/roles/roles_list.html",
        {
            "roles": roles,
            "active_nav": active_nav,
        },
    )


def roles_add_view(request):
    active_nav = "users"

    if request.method == "POST":
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:roles_list")
    else:
        form = RolesForm()

    return render(
        request,
        "users/roles/roles_add.html",
        {
            "form": form,
            "active_nav": active_nav,
        },
    )


def roles_edit_view(request, pk):
    role = get_object_or_404(Roles, pk=pk)
    active_nav = "users"

    if request.method == "POST":
        form = RolesForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect("users:roles_list")
    else:
        form = RolesForm(instance=role)

    return render(
        request,
        "users/roles/roles_edit.html",
        {
            "form": form,
            "active_nav": active_nav,
        },
    )


def roles_delete_view(request, pk):
    role = get_object_or_404(Roles, pk=pk)
    active_nav = "users"

    if request.method == "POST":
        role.delete()
        return redirect("users:roles_list")

    return render(
        request,
        "users/roles/roles_delete.html",
        {
            "role": role,
            "active_nav": active_nav,
        },
    )
