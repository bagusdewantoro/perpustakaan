# Generated by Django 3.1.2 on 2021-01-05 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0011_instancebuku_peminjam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instancebuku',
            options={'ordering': ['kembali'], 'permissions': (('bisa_tandai_kembali', 'Tandai bahwa sudah dikembalikan'),), 'verbose_name': 'Daftar Instance Buku', 'verbose_name_plural': 'Daftar Instance Buku'},
        ),
    ]