"""
URL configuration for webproje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
    path('arac_ekle/', views.arac_ekle, name='arac_ekle'),
    path('arac_sil/<int:arac_id>/', views.arac_sil, name='arac_sil'),
    path('arac_guncelle/<int:arac_id>/', views.arac_guncelle, name='arac_guncelle'),
    path('admin_arac_liste/', views.admin_arac_liste, name='admin_arac_liste'),
    path('admin_arac_sil/<int:arac_id>/', views.admin_arac_sil, name='admin_arac_sil'),
    path('admin_musteriler/', views.admin_musteriler, name='admin_musteriler'),
    path('musteri_sil/<int:musteri_id>/', views.musteri_sil, name='musteri_sil'),
    path('bilgilerimi_guncelle/', views.bilgilerimi_guncelle, name='bilgilerimi_guncelle'),


]
