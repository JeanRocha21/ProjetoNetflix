from django.contrib.auth.forms import UserCreationForm
from .models import usuarios
from django import forms

class FormHome(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = usuarios
        fields = ('username', 'email', 'password1', 'password2')
