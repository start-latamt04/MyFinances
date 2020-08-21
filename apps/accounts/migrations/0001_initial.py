# Generated by Django 3.1 on 2020-08-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10000000)),
                ('meta', models.DecimalField(decimal_places=2, default=0, max_digits=10000000)),
                ('gastos', models.DecimalField(decimal_places=2, default=0, max_digits=10000000)),
            ],
        ),
    ]
