from django.db import models
from django.contrib.auth.models import User    # memasukkan User, sehingga bisa dipakai di class-class di bawah ini
from datetime import date       # terkait dengan informasi tanggal peminjaman yang sudah lewat

class Jenis(models.Model):
    """Model untuk menyatakan jenis/aliran buku"""
    nama_jenis = models.CharField(max_length=200, \
                        help_text='Masukkan jenis buku (mis.: Sastra)')

    class Meta:
        ordering = ['nama_jenis']
        # Tambahkan Verbose Name (tambahkan 2 atribut dari class Meta di bawah ini)
        verbose_name = 'Pilihan Jenis'
        verbose_name_plural = 'Pilihan Jenis'

    def __str__(self):
        """String yang menyatakan object Model"""
        # yang akan ditampilkan di data admin
        return self.nama_jenis


class Bahasa(models.Model):
    """Model untuk menyatakan bahasa yang digunakan"""
    pilih_bahasa = models.CharField(max_length=20, \
                        help_text='Masukkan bahasa yang digunakan (mis.: Indonesia)')

    class Meta:
        ordering = ['pilih_bahasa']
        # Tambahkan Verbose Name (tambahkan 2 atribut dari class Meta di bawah ini)
        verbose_name = 'Pilihan Bahasa'
        verbose_name_plural = 'Pilihan Bahasa'

    def __str__(self):
        """String yang menyatakan object Model"""
        # yang akan ditampilkan di data admin
        return self.pilih_bahasa


# =======================
# class untuk model buku:
# =======================
from django.urls import reverse # generate URLs dengan membalikkan URL patterns
from django.utils.html import mark_safe #tampilkan gambar di admin

class Buku(models.Model):
    """Model untuk menyatakan sebuah buku"""
    judul = models.CharField(max_length=200)

    figure = models.ImageField(upload_to='static/img', null=True,
                                blank=True)

    # tampilkan gambar di admin
    @property
    def figure_preview(self):
        if self.figure:
            return mark_safe('<img src="{}" width="auto" height="100" />'.format(self.figure.url))
        return ""

    penulis = models.ForeignKey('Penulis', on_delete=models.SET_NULL, null=True)
    # pakai ForeignKey karena 1 buku hanya punya 1 penulis; tapi 1 penulis bisa punya banyak buku
    # penulis masih string, belum sebagai object

    resensi = models.TextField(max_length=1000, help_text='Tuliskan deskripsi singkat buku ini')
    isbn = models.CharField('ISBN', max_length=13, unique=True, \
                            help_text='13 Karakter <a href="https://www.isbn-international.org/content/what-isbn">nomor ISBN</a>')

    jenis = models.ManyToManyField(Jenis, help_text='Pilih jenis/aliran buku ini')
    # pakai ManyToManyField karena 1 jenis/aliran bisa mencakup banyak buku; 1 buku bisa mencakup banyak jenis/aliran
    # class Jenis sudah ditentukan. Jadi kita bisa menentukan objek di atas

    bahasa = models.ForeignKey('Bahasa', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['judul']
        # Tambahkan Verbose Name (tambahkan 2 atribut dari class Meta di bawah ini)
        verbose_name = 'Buku'
        verbose_name_plural = 'Buku'

    def __str__(self):
        """String yang menyatakan object Model"""
        # yang akan ditampilkan di data admin
        return self.judul

    def get_absolute_url(self):
        """Return url untuk mengakses detail dari buku ini"""
        return reverse('detail-buku', args=[str(self.id)])

    # Tambahan method untuk menampilkan jenis buku Admin
    def jenis_buku(self):
        """Membuat string untuk class Jenis. Ini diperlukan untuk menampilkan jenis di admin"""
        return ', '.join(jenis.nama_jenis for jenis in self.jenis.all()[:3])
    jenis_buku.short_description = 'Jenis Buku'


# =======================
# class untuk model instance (copy-an) buku:
# =======================
import uuid  # python module = Universally Unique Identifiers

class InstanceBuku(models.Model):
    """Model untuk menyatakan copy-an tertentu dari sebuah buku (yang mungkin sedang dipinjam di perpustakaan)"""
    id = models.UUIDField('Kode Copy', primary_key=True, default=uuid.uuid4, \
                        help_text='Kode unik untuk buku tertentu di seluruh perpustakaan')
    buku = models.ForeignKey('Buku', verbose_name='Judul Buku', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    kembali = models.DateField('Tanggal Pengembalian', null=True, blank=True)

    STATUS_SEWA = (
        ('p', 'diperbaiki'),
        ('s', 'disewa'),
        ('a', 'ada'),
        ('b', 'dipesan'),
    )

    status = models.CharField('Status Buku', max_length=1, choices=STATUS_SEWA, blank=True, \
                            default='p', help_text='Ketersediaan buku')

    # menghubungkan User dengan Book Instance:
    peminjam = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['kembali']
        # Tambahkan Verbose Name (tambahkan 2 atribut dari class Meta di bawah ini)
        verbose_name = 'Daftar Instance Buku'
        verbose_name_plural = 'Daftar Instance Buku'
        # data permission = tuple (nama permission, nama yang ditampilkan)
        permissions = (("bisa_tandai_kembali", "Tandai bahwa sudah dikembalikan"),)

    # menampilkan informasi jika tanggal pengembalian sudah lewat:
    @property
    def terlambat(self):
        if self.kembali and date.today() > self.kembali:
            return True
        return False

    def __str__(self):
        """String yang menyatakan object Model"""
        # yang akan ditampilkan di data admin
        return f'{self.id} ({self.buku.judul})'


# =====================
# class untuk penulis:
# =====================
class Penulis(models.Model):
    """Model yang menyatakan penulis"""
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(null=True, blank=True)
    tanggal_wafat = models.DateField('Wafat', null=True, blank=True)

    class Meta:
        ordering = ['nama_belakang', 'nama_depan']
        # Tambahkan Verbose Name (tambahkan 2 atribut dari class Meta di bawah ini)
        verbose_name = 'Daftar Penulis'
        verbose_name_plural = 'Daftar Penulis'

    def __str__(self):
        """String yang menyatakan object Model"""
        # yang akan ditampilkan di data admin
        return f'{self.nama_belakang}, {self.nama_depan}'

    def get_absolute_url(self):
        """Return URL untuk mengakses instansce pengarang tertentu"""
        return reverse('detail-penulis', args=[str(self.id)])
