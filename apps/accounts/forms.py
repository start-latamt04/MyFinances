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
        fields = ['saldo', 'meta', 'gastos', 'descricao']


'''class MesesForm(forms.Form):
    CHOICES = (('1', 'Janeiro'), ('2', 'Fevereiro'), ('3', 'Março'), ('4', 'Abril'), ('5', 'Maio'), ('6', 'Junho'),
               ('7', 'Julho'), ('8', 'Agosto'), ('9', 'Setembro'), ('10', 'Outubro'), ('11', 'Novembro'),
               ('12', 'Desembro'))
    select = forms.CharField(widget=forms.Select(choices=CHOICES))
'''