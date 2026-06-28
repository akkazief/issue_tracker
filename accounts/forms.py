from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name", "").strip()
        last_name = cleaned_data.get("last_name", "").strip()

        if not first_name and not last_name:
            raise ValidationError("Хотя бы одно из полей: Имя или Фамилия должно быть заполнено")

        return cleaned_data