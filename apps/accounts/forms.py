from django import forms
from django.contrib.auth.models import User

from .models import Saldo
#from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']


#criação de form para saldo/gasto

class SaldoForm(forms.ModelForm):
    saldo = forms.DecimalField(max_digits=10000000, decimal_places=2, localize=True)
    meta = forms.DecimalField(max_digits=10000000, decimal_places=2, localize=True)
    gastos = forms.DecimalField(max_digits=10000000, decimal_places=2, localize=True)
    class Meta():
        model = Saldo
        fields = ['saldo', 'meta', 'gastos']