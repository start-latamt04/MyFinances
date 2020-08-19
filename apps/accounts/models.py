from django.db import models


class Saldo(models.Model):
    saldo = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    meta = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    gastos = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
