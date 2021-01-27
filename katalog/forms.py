import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PerbaruiBukuForm(forms.Form):
    perbarui_tanggal = forms.DateField(help_text="Masukkan tanggal antara sekarang dan 4 minggu ke depan (default 3).")

    def clean_perbarui_tanggal(self):   # clean_<field> = validate
        data = self.cleaned_data['perbarui_tanggal']

        # cek jika tanggalnya lebih baru (bukan tanggal yang sudah lewat)
        if data < datetime.date.today():
            raise ValidationError(_('Salah tanggal - tanggalnya sudah lewat'))

        # cek jika tanggalnya sudah sesuai dengan range (+4 minggu dari dari sekarang)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Salah tanggal - tanggalnya lebih dari 4 minggu ke depan'))

        # ingat untuk selalu return cleaned data:
        return data
