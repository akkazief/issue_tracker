from django import forms
from issues.models.issue import Issue
from issues.models.status import Status
from issues.models.type import Type


from issues.validators import validate_summary_length, validate_exlude_words


class IssueForm(forms.ModelForm):
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
            "type": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        validate_summary_length(summary)
        validate_exlude_words(summary)
        return summary
