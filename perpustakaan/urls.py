"""perpustakaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# include() untuk menambahkan path dari aplikasi katalog
from django.urls import include
urlpatterns += [
    path('katalog/', include('katalog.urls')),
]

# tambahkan url maps untuk redirect dari base URL ke URL aplikasi
# jadi dari <base_url>/   bisa langsung ke <base_url>/katalog/
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='katalog/', permanent=True)),
]

# tambahkan static() ke url mapping untuk serve static saat development (only)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# tambahkan gambar
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
