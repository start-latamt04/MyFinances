# Generated by Django 3.1 on 2020-08-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200826_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saldo',
            old_name='user_id',
            new_name='user',
        ),
    ]