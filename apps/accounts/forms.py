from django import forms
from django.contrib.auth.models import User

from .models import Saldo


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']


# criação de form para saldo/gasto

class SaldoForm(forms.ModelForm):

    class Meta:
        model = Saldo
<<<<<<< HEAD
        fields = ['saldo', 'meta', 'gastos', 'descricao']
=======
        fields = ['saldo', 'meta', 'gastos']
>>>>>>> b5f7c016f9f4c1df5264a2d7ba610211455a8856
