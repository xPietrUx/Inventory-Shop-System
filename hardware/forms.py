from django import forms
from .models import Hardware, HardwareHistory, Project


class HardwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False
        self.fields["project"].required = False

    class Meta:
        model = Hardware
        fields = [
            "inventory_number",
            "name",
            "category",
            "serial_number",
            "purchase_date",
            "warranty_to",
            "status",
            "user",
            "project",
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
        fields = ["name", "description", "supervisor", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
