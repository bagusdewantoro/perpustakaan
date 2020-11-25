from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('koleksi/', views.BukuListView.as_view(), name='koleksi'),
    path('buku/<int:pk>', views.BukuDetailView.as_view(), name='detail-buku'),
]
