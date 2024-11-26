from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MedicoCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Primeiro Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Último Nome')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password1', 'password2')  # Inclui os campos de senha
