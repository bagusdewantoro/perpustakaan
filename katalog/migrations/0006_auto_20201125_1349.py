# Generated by Django 3.1.2 on 2020-11-25 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_auto_20201125_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instancebuku',
            old_name='kode',
            new_name='id',
        ),
    ]