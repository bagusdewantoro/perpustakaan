from django.urls import path
from . import views

urlpatterns = [
    # basic pages:
    path('', views.index, name='index'),
    path('koleksi/', views.BukuListView.as_view(), name='koleksi'),
    path('koleksi/<int:pk>', views.BukuDetailView.as_view(), name='detail-buku'),
    path('penulis/', views.PenulisListView.as_view(), name='penulis'),
    path('penulis/<int:pk>', views.PenulisDetailView.as_view(), name='detail-penulis'),

    # authentication:
    path('bukuku/', views.BukuDisewaUserListView.as_view(), name='pinjamanku'),
    path(r'dipinjam/', views.SeluruhBukuDipinjamListView.as_view(), name='seluruh-pinjaman'),

    # forms perbarui data buku pinjaman:
    path('koleksi/<uuid:pk>/perbarui', views.perbarui_buku_pustakawan, name='perbarui-buku-pustakawan'),

    # forms edit penulis:
    path('penulis/buat/', views.PenulisCreate.as_view(), name='penulis-create'),
    path('penulis/<int:pk>/perbarui/', views.PenulisUpdate.as_view(), name='penulis-update'),
    path('penulis/<int:pk>/hapus/', views.PenulisDelete.as_view(), name='penulis-delete'),

    # forms edit buku:
    path('koleksi/buat/', views.BukuCreate.as_view(), name='koleksi-create'),
    path('koleksi/<int:pk>/perbarui/', views.BukuUpdate.as_view(), name='koleksi-update'),
    path('koleksi/<int:pk>/hapus/', views.BukuDelete.as_view(), name='koleksi-delete'),    
]
