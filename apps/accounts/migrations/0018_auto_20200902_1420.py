# Generated by Django 3.1 on 2020-09-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200902_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
