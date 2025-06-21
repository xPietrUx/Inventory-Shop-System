from django.shortcuts import render, get_object_or_404, redirect
from .models import Hardware, Project, HardwareHistory
from .forms import HardwareForm, HardwareHistoryForm, ProjectForm
from django.contrib.auth.decorators import login_required

# ===========================
# Views dla modelu hardware
# ===========================


@login_required
def hardware_list_view(request):
    hardware_list = Hardware.objects.all()
    active_nav = "hardware"
    active_page_title = "Hardware List"
    return render(
        request,
        "hardware/hardware/hardware_list.html",
        {
            "hardware_list": hardware_list,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def hardware_add_view(request):
    if request.method == "POST":
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hardware:hardware_list")
    else:
        form = HardwareForm()

    active_nav = "hardware"
    active_page_title = "Add Hardware"

    return render(
        request,
        "hardware/hardware/hardware_add.html",
        {
            "form": form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def hardware_edit_view(request, pk):
    hardware_item = get_object_or_404(Hardware, pk=pk)

    if request.method == "POST":
        form = HardwareForm(request.POST, instance=hardware_item)
        if form.is_valid():
            form.save()
            return redirect("hardware:hardware_list")
    else:
        form = HardwareForm(instance=hardware_item)

    active_nav = "hardware"
    active_page_title = f"Edit Hardware: {hardware_item.name}"

    return render(
        request,
        "hardware/hardware/hardware_edit.html",
        {
            "form": form,
            "hardware_item": hardware_item,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def hardware_delete_view(request, pk):
    hardware_item = get_object_or_404(Hardware, pk=pk)

    if request.method == "POST":
        hardware_item.delete()
        return redirect("hardware:hardware_list")

    active_nav = "hardware"
    active_page_title = "Delete Hardware"

    return render(
        request,
        "hardware/hardware/hardware_delete.html",
        {
            "hardware_item": hardware_item,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


# ===========================
# Views dla modelu history
# ===========================


@login_required
def history_list_view(request):
    history_list = HardwareHistory.objects.all().order_by("-event_date")
    active_nav = "hardware"
    active_page_title = "Hardware History"
    return render(
        request,
        "hardware/history/history_list.html",
        {
            "history_list": history_list,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


# ===========================
# Views dla modelu project
# ===========================


@login_required
def project_list_view(request):
    project_list = Project.objects.all()
    active_nav = "hardware"
    active_page_title = "Projects"
    return render(
        request,
        "hardware/projects/projects_list.html",
        {
            "project_list": project_list,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def project_add_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hardware:project_list")
    else:
        form = ProjectForm()

    active_nav = "hardware"
    active_page_title = "Add Project"

    return render(
        request,
        "hardware/projects/projects_add.html",
        {
            "form": form,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def project_edit_view(request, pk):
    project_item = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project_item)
        if form.is_valid():
            form.save()
            return redirect("hardware:project_list")
    else:
        form = ProjectForm(instance=project_item)

    active_nav = "hardware"
    active_page_title = f"Edit Project: {project_item.name}"

    return render(
        request,
        "hardware/projects/projects_edit.html",
        {
            "form": form,
            "project_item": project_item,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )


@login_required
def project_delete_view(request, pk):
    project_item = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        project_item.delete()
        return redirect("hardware:project_list")

    active_nav = "hardware"
    active_page_title = "Delete Project"

    return render(
        request,
        "hardware/projects/projects_delete.html",
        {
            "project_item": project_item,
            "active_nav": active_nav,
            "active_page_title": active_page_title,
        },
    )
