# Generated by Django 3.1.2 on 2020-12-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0009_auto_20201201_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='sampul',
        ),
        migrations.AddField(
            model_name='buku',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]