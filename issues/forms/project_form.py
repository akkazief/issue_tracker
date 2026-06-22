from issues.models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "start_date", "end_date")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Название проекта",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Описание проекта",
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Начало проекта",
                    "type": "date",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Окончание проекта",
                }
            ),
        }
