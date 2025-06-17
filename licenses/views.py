from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # Dodaj ten import dla placeholderów
from .models import Software, License


# Widoki dla modelu Software
def software_list_view(request):
    software_items = Software.objects.all()
    # Możesz dodać logikę sortowania na podstawie request.GET.get('sort')
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


def software_add_view(request):
    # Tutaj logika formularza dodawania
    # from .forms import SoftwareForm # Przykładowy import formularza
    # form = SoftwareForm()
    active_nav = "software"
    active_page_title = "Dodaj Oprogramowanie"
    # Upewnij się, że szablon 'licenses/software/software_add.html' istnieje
    return render(
        request,
        "licenses/software/software_add.html",  # Upewnij się, że ten szablon istnieje
        {
            # 'form': form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def software_edit_view(request, pk):
    software_instance = get_object_or_404(Software, pk=pk)
    # Tutaj logika formularza edycji
    active_nav = "software"
    active_page_title = f"Edytuj Oprogramowanie: {software_instance.name}"
    # Upewnij się, że szablon 'licenses/software/software_edit.html' istnieje
    return render(
        request,
        "licenses/software/software_edit.html",  # Upewnij się, że ten szablon istnieje
        {
            # 'form': form_instance,
            "software": software_instance,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def software_delete_view(request, pk):
    software_instance = get_object_or_404(Software, pk=pk)
    # Tutaj logika potwierdzenia usunięcia i usuwania
    active_nav = "software"
    active_page_title = f"Usuń Oprogramowanie: {software_instance.name}"
    # Upewnij się, że szablon 'licenses/software/software_delete.html' istnieje
    return render(
        request,
        "licenses/software/software_delete.html",  # Upewnij się, że ten szablon istnieje
        {
            "software": software_instance,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


# Widoki dla modelu License
def license_list_view(request):
    license_items = License.objects.all()
    active_nav = "licenses"
    active_page_title = "Licencje"
    # Upewnij się, że szablon 'licenses/license/license_list.html' istnieje
    return render(
        request,
        "licenses/license/license_list.html",  # Upewnij się, że ten szablon istnieje
        {
            "license_list": license_items,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def license_add_view(request):
    active_nav = "licenses"
    active_page_title = "Dodaj Licencję"
    # Upewnij się, że szablon 'licenses/license/license_add.html' istnieje
    # Ten szablon ma już jakąś zawartość, więc renderujemy go
    return render(
        request,
        "licenses/license/license_add.html",
        {"active_nav": active_nav, "active_page_title": active_page_title},
    )


def license_edit_view(request, pk):
    license_instance = get_object_or_404(License, pk=pk)
    active_nav = "licenses"
    active_page_title = f"Edytuj Licencję: {license_instance.license_key}"
    # Upewnij się, że szablon 'licenses/license/license_edit.html' istnieje
    return render(
        request,
        "licenses/license/license_edit.html",  # Upewnij się, że ten szablon istnieje
        {
            "license_item": license_instance,  # Zmieniono nazwę zmiennej kontekstowej
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


def license_delete_view(request, pk):
    license_instance = get_object_or_404(License, pk=pk)
    active_nav = "licenses"
    active_page_title = f"Usuń Licencję: {license_instance.license_key}"
    # Upewnij się, że szablon 'licenses/license/license_delete.html' istnieje
    return render(
        request,
        "licenses/license/license_delete.html",  # Upewnij się, że ten szablon istnieje
        {
            "license_item": license_instance,  # Zmieniono nazwę zmiennej kontekstowej
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )
