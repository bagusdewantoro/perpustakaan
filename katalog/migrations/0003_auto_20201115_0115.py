# Generated by Django 3.1.2 on 2020-11-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20201114_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bahasa',
            options={'verbose_name': 'Pilihan Bahasa', 'verbose_name_plural': 'Pilihan Bahasa'},
        ),
        migrations.AlterModelOptions(
            name='buku',
            options={'verbose_name': 'Buku', 'verbose_name_plural': 'Buku'},
        ),
        migrations.AlterModelOptions(
            name='instancebuku',
            options={'ordering': ['kembali'], 'verbose_name': 'Daftar Instance Buku', 'verbose_name_plural': 'Daftar Instance Buku'},
        ),
        migrations.AlterModelOptions(
            name='jenis',
            options={'verbose_name': 'Pilihan Jenis', 'verbose_name_plural': 'Pilihan Jenis'},
        ),
        migrations.AlterModelOptions(
            name='penulis',
            options={'ordering': ['nama_belakang', 'nama_depan'], 'verbose_name': 'Daftar Penulis', 'verbose_name_plural': 'Daftar Penulis'},
        ),
        migrations.RenameField(
            model_name='jenis',
            old_name='nama',
            new_name='nama_jenis',
        ),
    ]
