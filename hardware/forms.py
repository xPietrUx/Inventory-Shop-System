from django import forms
from .models import Hardware, HardwareHistory, Project


class HardwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_id"].required = False
        self.fields["project_id"].required = False

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


class HardwareHistoryForm(forms.ModelForm):
    class Meta:
        model = HardwareHistory
        fields = ["event_date", "event_type", "description"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "supervisor_id", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
