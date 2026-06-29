from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectMembersForm(forms.Form):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,required=False)