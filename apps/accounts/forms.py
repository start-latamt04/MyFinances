from django import forms
from django.contrib.auth.models import User

from .models import Saldo


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']



class SaldoForm(forms.ModelForm):

    class Meta:
        model = Saldo

        fields = ['saldo', 'meta', 'gastos', 'descricao']