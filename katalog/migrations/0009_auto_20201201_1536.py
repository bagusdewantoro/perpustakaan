# Generated by Django 3.1.2 on 2020-12-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0008_auto_20201129_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='sampul',
            field=models.ImageField(null=True, upload_to='gambar'),
        ),
    ]
