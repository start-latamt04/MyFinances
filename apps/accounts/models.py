from django.contrib.auth.models import User
from django.db import models


class Saldo(models.Model):

    saldo = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    meta = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    gastos = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    descricao = models.TextField(max_length=40, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.gastos, self.descricao