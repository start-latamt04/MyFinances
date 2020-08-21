from django.db import models
from django.db.models import DateTimeField


class Saldo(models.Model):


    saldo = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    meta = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    gastos = models.DecimalField(max_digits=10000000, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.gastos