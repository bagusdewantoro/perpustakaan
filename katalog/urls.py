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
    # forms:
    path('koleksi/<uuid:pk>/perbarui', views.perbarui_buku_pustakawan, name='perbarui-buku-pustakawan')
]
