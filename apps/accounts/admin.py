from django.contrib import admin
from .models import Saldo


class SaldoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Saldo, SaldoAdmin)
