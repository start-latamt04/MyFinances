from django.db import models

from django.contrib.auth import get_user_model


class Saldo(models.Model):

    saldo = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    meta = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    gastos = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    descricao = models.TextField(max_length=40, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gastos, self.descricao
    saldo = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    meta = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    gastos = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.gastos
