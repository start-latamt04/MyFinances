from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Saldo(models.Model):

    saldo = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    meta = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    gastos = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    descricao = models.TextField(max_length=40, null=True, default="")
    created_at = models.DateTimeField(auto_now=True)
    total_gastos = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.gastos} {self.descricao}'


class Usuario(AbstractUser):
    email = models.EmailField(null=False, unique=True)
