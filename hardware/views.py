from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import HardwareForm, HardwareHistoryForm, ProjectForm
from .models import Hardware, HardwareCategory, Project, HardwareHistory
from django.contrib.auth import get_user_model

User = get_user_model()

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = [
            "inventory_number",
            "name",
            "category_id",
            "serial_number",
            "purchase_date",
            "warranty_to",
            "status",
            "user_id",
            "project_id",
        ]
        widgets = {
            "purchase_date": forms.DateInput(attrs={"type": "date"}),
            "warranty_to": forms.DateInput(attrs={"type": "date"}),
        }

class HardwareListView(ListView):
    model = Hardware
    template_name = "hardware/hardware/hardware_list.html"
    context_object_name = "hardware_list"

class HardwareAddView(CreateView):
    model = Hardware
    form_class = HardwareForm
    template_name = "hardware/hardware/hardware_add.html"
    success_url = reverse_lazy("hardware:hardware_list")

class HardwareEditView(UpdateView):
    model = Hardware
    form_class = HardwareForm
    template_name = "hardware/hardware/hardware_edit.html"
    success_url = reverse_lazy("hardware:hardware_list")

class HardwareDeleteView(DeleteView):
    model = Hardware
    template_name = "hardware/hardware/hardware_delete.html"
    success_url = reverse_lazy("hardware:hardware_list")

class HardwareHistoryForm(forms.ModelForm):
    class Meta:
        model = HardwareHistory
        fields = ["event_date", "event_type", "description"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }

class HardwareHistoryListView(ListView):
    model = HardwareHistory
    template_name = "hardware/history/hardware_history_list.html"
    context_object_name = "history_list"

    def get_queryset(self):
        return HardwareHistory.objects.filter(hardware_id=self.kwargs['hardware_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hardware'] = Hardware.objects.get(pk=self.kwargs['hardware_id'])
        context['form'] = HardwareHistoryForm()
        return context

    def post(self, request, *args, **kwargs):
        form = HardwareHistoryForm(request.POST)
        if form.is_valid():
            history_entry = form.save(commit=False)
            history_entry.hardware_id = Hardware.objects.get(pk=self.kwargs['hardware_id'])
            history_entry.save()
        return self.get(request, *args, **kwargs)

class HardwareHistoryEditView(UpdateView):
    model = HardwareHistory
    form_class = HardwareHistoryForm
    template_name = "hardware/history/hardware_history_edit.html"

    def get_success_url(self):
        return reverse_lazy(
            "hardware:hardware_history",
            kwargs={"hardware_id": self.object.hardware_id.pk},
        )

class HardwareHistoryDeleteView(DeleteView):
    model = HardwareHistory
    template_name = "hardware/history/hardware_history_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "hardware:hardware_history",
            kwargs={"hardware_id": self.object.hardware_id.pk},
        )


# --------------------------- PROJECTS ----------------------------------------------------------------


class ProjectListView(ListView):
    model = Project
    template_name = "hardware/projects/project_list.html"
    context_object_name = "projects"


class ProjectAddView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "hardware/projects/project_add.html"
    success_url = reverse_lazy("hardware:project_list")


class ProjectEditView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "hardware/projects/project_edit.html"
    success_url = reverse_lazy("hardware:project_list")


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "hardware/projects/project_delete.html"
    success_url = reverse_lazy("hardware:project_list")
