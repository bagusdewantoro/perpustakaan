# Generated by Django 3.1.2 on 2020-11-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bahasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(help_text='Masukkan bahasa yang digunakan (mis.: Indonesia)', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='jenis',
            name='nama',
            field=models.CharField(help_text='Masukkan jenis buku (mis.: Sastra)', max_length=200),
        ),
        migrations.AddField(
            model_name='buku',
            name='bahasa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.bahasa'),
        ),
    ]