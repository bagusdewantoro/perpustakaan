from django.contrib import admin

# import the models and register them
from .models import Jenis, Bahasa, Buku, InstanceBuku, Penulis


# Cara dasar untuk register models :
admin.site.register(Jenis)
admin.site.register(Bahasa)
# admin.site.register(Buku)
# admin.site.register(InstanceBuku)
# admin.site.register(Penulis)


# tampilkan informasi buku dalam halaman detail penulis
class BukuInline(admin.StackedInline):
    model = Buku
    extra = 0

# define class admin untuk Penulis:
class PenulisAdmin(admin.ModelAdmin):
    list_display = ('nama_belakang', 'nama_depan', 'tanggal_lahir', 'tanggal_wafat') # display kolom field
    fields = ['nama_depan', 'nama_belakang', ('tanggal_lahir', 'tanggal_wafat')] # bisa display dalam grup (tuple)
    inlines = [BukuInline] # menambahkan class BukuInline. class Buku HARUS punya ForeignKey ke Penulis
# lalu register admin class dengan model terkait:
admin.site.register(Penulis, PenulisAdmin)


# tampilkan informasi instance buku dalam halaman detail buku
class InstanceInline(admin.TabularInline):
    model = InstanceBuku
    extra = 1   # menambahkan 2 placeholder untuk instancebuku yang baru. Not Recommended!
    # by default, ada tambahan 3 placeholder. Sebaiknya dibikin jadi 0 saja.

# syntax lain yang sifatnya sama persis dengan admin.site.register() :
# define class admin untuk Buku dan InstanceBuku:
@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'jenis_buku') # display kolom field
    inlines = [InstanceInline] # menambahkan class InstanceInline. class InstanceBuku HARUS punya ForeignKey ke Buku


@admin.register(InstanceBuku)
class InstanceBukuAdmin(admin.ModelAdmin):
    list_filter = ('status', 'kembali') # display filter box
    list_display = ('buku', 'kode', 'status')

    fieldsets = (
        (None, {'fields': ('buku', 'imprint', 'kode')}),
        ('Ketersediaan', {'fields': ('status', 'kembali')})
    )
