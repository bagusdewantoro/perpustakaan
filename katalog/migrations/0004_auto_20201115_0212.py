# Generated by Django 3.1.2 on 2020-11-14 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0003_auto_20201115_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bahasa',
            old_name='nama',
            new_name='pilih_bahasa',
        ),
    ]