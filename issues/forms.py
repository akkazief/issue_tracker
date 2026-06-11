from django import forms
from issues.models.issue import Issue
from issues.models.status import Status
from issues.models.type import Type


class IssueForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())

    class Meta:
        model = Issue
        fields = ("summary", "description", "status", "type")
        widgets = {
            "summary": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Краткое описание задачи",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Полное описание задачи",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "type": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
