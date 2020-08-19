from django import forms
from django.contrib.auth.models import User
<<<<<<< HEAD

from .models import Saldo
#from .models import *

=======
from .models import Saldo

# from .models import *

>>>>>>> e18b584c4e3c580cb2470f59acdbb6648dd18642

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']


# criação de form para saldo/gasto

class SaldoForm(forms.ModelForm):
    saldo = forms.DecimalField(max_digits=10000000, decimal_places=2, localize=True)
    meta = forms.DecimalField(max_digits=10000000, decimal_places=2, localize=True)
    gastos = forms.DecimalField(max_digits=10000000, decimal_places=2, localize=True)

    class Meta:
        model = Saldo
        fields = ['saldo', 'meta', 'gastos']
