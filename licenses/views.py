from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import Software, License
from django.contrib.auth.decorators import login_required


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ["name", "producer"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Software name"}
            ),
            "producer": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Producer"}
            ),
        }


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = [
            "software_id",
            "license_key",
            "user_id",
            "purchase_date",
            "expiration_date",
            "license_type",
        ]
        widgets = {
            "purchase_date": forms.DateInput(attrs={"type": "date"}),
            "expiration_date": forms.DateInput(attrs={"type": "date"}),
        }


# ===========================
# Widoki dla modelu Software
# ===========================


@login_required
def software_list_view(request):
    software_items = Software.objects.all()
    active_nav = "software"
    active_page_title = "Oprogramowanie"
    return render(
        request,
        "licenses/software/software_list.html",
        {
            "software_list": software_items,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def software_add_view(request):
    active_nav = "software"
    active_page_title = "Dodaj Oprogramowanie"
    if request.method == "POST":
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("licenses:software_list")
    else:
        form = SoftwareForm()
    return render(
        request,
        "licenses/software/software_add.html",
        {
            "form": form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def software_edit_view(request, pk):
    software_instance = get_object_or_404(Software, pk=pk)
    active_nav = "software"
    active_page_title = f"Edytuj Oprogramowanie: {software_instance.name}"

    if request.method == "POST":
        form = SoftwareForm(request.POST, instance=software_instance)
        if form.is_valid():
            form.save()
            return redirect("licenses:software_list")
    else:
        form = SoftwareForm(instance=software_instance)

    return render(
        request,
        "licenses/software/software_edit.html",
        {
            "form": form,
            "software": software_instance,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def software_delete_view(request, pk):
    software_instance = get_object_or_404(Software, pk=pk)
    active_nav = "software"
    active_page_title = f"Usuń Oprogramowanie: {software_instance.name}"

    if request.method == "POST":
        software_instance.delete()
        return redirect("licenses:software_list")

    return render(
        request,
        "licenses/software/software_delete.html",
        {
            "software": software_instance,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


# ===========================
# Widoki dla modelu License
# ===========================


@login_required
def license_list_view(request):
    license_items = License.objects.all()
    active_nav = "licenses"
    active_page_title = "Licencje"
    return render(
        request,
        "licenses/license/license_list.html",
        {
            "license_list": license_items,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def license_add_view(request):
    active_nav = "licenses"
    active_page_title = "Dodaj Licencję"
    if request.method == "POST":
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("licenses:license_list")
    else:
        form = LicenseForm()
    return render(
        request,
        "licenses/license/license_add.html",
        {
            "form": form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def license_edit_view(request, pk):
    license_instance = get_object_or_404(License, pk=pk)
    active_nav = "licenses"
    active_page_title = f"Edytuj Licencję: {license_instance.license_key}"

    if request.method == "POST":
        form = LicenseForm(request.POST, instance=license_instance)
        if form.is_valid():
            form.save()
            return redirect("licenses:license_list")
    else:
        form = LicenseForm(instance=license_instance)

    return render(
        request,
        "licenses/license/license_edit.html",
        {
            "form": form,
            "license_item": license_instance,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def license_delete_view(request, pk):
    license_instance = get_object_or_404(License, pk=pk)
    active_nav = "licenses"
    active_page_title = f"Usuń Licencję: {license_instance.license_key}"

    if request.method == "POST":
        license_instance.delete()
        return redirect("licenses:license_list")

    return render(
        request,
        "licenses/license/license_delete.html",
        {
            "license_item": license_instance,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )
