from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('koleksi/', views.BukuListView.as_view(), name='koleksi'),
    path('koleksi/<int:pk>', views.BukuDetailView.as_view(), name='detail-buku'),
    path('penulis/', views.PenulisListView.as_view(), name='penulis'),
    path('penulis/<int:pk>', views.PenulisDetailView.as_view(), name='detail-penulis')
]
