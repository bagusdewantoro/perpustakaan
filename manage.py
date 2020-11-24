#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perpustakaan.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Mengganti nama field di models tanpa kehilangan data
# Jika mengganti nama field pada salah satu class di file models.py :
# Contoh : class Bahasa. Ganti field nama menjadi pilih_bahasa
# Sebelum menulis kode di bawah, laukakan py manage.py makemigrations
# Lalu tulis kode di bawah, save. Lalu lakukan py manage.py migrate
#from django.db import migrations
#operations = [
#    migrations.RenameField(
#        model_name='Bahasa',
#        old_name='nama',
#        new_name='pilih_bahasa')
#]


if __name__ == '__main__':
    main()
