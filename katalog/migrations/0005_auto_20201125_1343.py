# Generated by Django 3.1.2 on 2020-11-25 06:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0004_auto_20201115_0212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bahasa',
            options={'ordering': ['pilih_bahasa'], 'verbose_name': 'Pilihan Bahasa', 'verbose_name_plural': 'Pilihan Bahasa'},
        ),
        migrations.AlterModelOptions(
            name='jenis',
            options={'ordering': ['nama_jenis'], 'verbose_name': 'Pilihan Jenis', 'verbose_name_plural': 'Pilihan Jenis'},
        ),
        migrations.AlterField(
            model_name='instancebuku',
            name='buku',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.buku', verbose_name='Judul Buku'),
        ),
        migrations.AlterField(
            model_name='instancebuku',
            name='kembali',
            field=models.DateField(blank=True, null=True, verbose_name='Tanggal Pengembalian'),
        ),
        migrations.AlterField(
            model_name='instancebuku',
            name='kode',
            field=models.UUIDField(default=uuid.uuid4, help_text='Kode unik untuk buku tertentu di seluruh perpustakaan', primary_key=True, serialize=False, verbose_name='Kode Copy'),
        ),
        migrations.AlterField(
            model_name='instancebuku',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'diperbaiki'), ('s', 'disewa'), ('a', 'ada'), ('b', 'dipesan')], default='p', help_text='Ketersediaan buku', max_length=1, verbose_name='Status Buku'),
        ),
    ]
