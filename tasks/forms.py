from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description' ,'status', 'deadline')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше описание',}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Поле для детального описания'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            })
        }