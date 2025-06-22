from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Role
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from utils.decorators import role_required

# about views


def about_view(request):
    active_nav = "about"
    active_page_title = "About"
    return render(
        request,
        "about.html",
        {
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "position",
            "role",
            "email",
            "username",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "First Name"},
            ),
            "last_name": forms.TextInput(
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
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.password = make_password(password)
        if commit:
            user.save()
        return user


class UserAddForm(UserBaseForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}), required=True
    )

    class Meta(UserBaseForm.Meta):
        fields = UserBaseForm.Meta.fields


class UserEditForm(UserBaseForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Leave blank to keep the current password."}
        ),
        required=False,
    )

    class Meta(UserBaseForm.Meta):
        fields = UserBaseForm.Meta.fields


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = [
            "name",
            "description",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "description": forms.TextInput(attrs={"placeholder": "Description"}),
        }


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }


# users views
@login_required
@role_required("Admin", redirect_to="hardware:hardware_list")
def users_list_view(request):
    users = User.objects.all()
    active_nav = "users"
    active_page_title = "User"

    return render(
        request,
        "users/users/users_list.html",
        {
            "users": users,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
@role_required("Admin", redirect_to="hardware:hardware_list")
def users_add_view(request):
    active_nav = "users"
    active_page_title = "User"

    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:users_list")
    else:
        form = UserAddForm()

    return render(
        request,
        "users/users/users_add.html",
        {
            "form": form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
@role_required("Admin", redirect_to="hardware:hardware_list")
def users_edit_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    active_nav = "users"
    active_page_title = f"Edit User: {user.username}"

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users:users_list")

    else:
        form = UserEditForm(instance=user)

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


@login_required
@role_required("Admin", redirect_to="hardware:hardware_list")
def users_delete_view(request, pk):
    user = get_object_or_404(User, pk=pk)
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
@login_required
@role_required("Admin", redirect_to="hardware:hardware_list")
def roles_list_view(request):
    roles = Role.objects.all()
    active_nav = "users"

    return render(
        request,
        "users/roles/roles_list.html",
        {
            "roles": roles,
            "active_nav": active_nav,
        },
    )


# auth views
def signin_view(request):
    active_nav = "sign_in"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("users:users_list")
        else:
            return redirect("users:signin")
    else:
        form = SigninForm()

    return render(
        request,
        "auth/signin.html",
        {
            "form": form,
            "active_nav": active_nav,
        },
    )


def signout_view(request):
    logout(request)
    return redirect("users:signin")
