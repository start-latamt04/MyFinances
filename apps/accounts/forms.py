from django import forms
from django.contrib.auth import get_user_model

from .models import Saldo

User = get_user_model()


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado!')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']


# criação de form para saldo/gasto

class SaldoForm(forms.ModelForm):

    class Meta:
        model = Saldo
        fields = ['saldo', 'meta', 'gastos', 'descricao']


