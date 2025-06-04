"""
URL configuration for proje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from uygulama import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa, name='anasayfa'),
    path('araclar/', views.arac_listesi, name='arac_listesi'),
    path('arac_ekle/', views.arac_ekle, name='arac_ekle'),
    path('arac_sil/<int:arac_id>/', views.arac_sil, name='arac_sil'),
    path('admin_paneli/', views.admin_paneli, name='admin_paneli'),
    path('admin_arac_liste/', views.admin_arac_liste, name='admin_arac_liste'),  # Yeni URL
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('rezervasyon/<int:arac_id>/', views.rezervasyon, name='rezervasyon'),
    path('musteri_login/', views.musteri_login, name='musteri_login'),
    path('musteri_logout/', views.musteri_logout, name='musteri_logout'),
    path('musteri_register/', views.musteri_register, name='musteri_register'),
    path('musteri_paneli/', views.musteri_paneli, name='musteri_paneli'),  # Müşteri Paneli URL tanımı
    path('musteri_kayit/', views.musteri_register, name='musteri_kayit'),
    path('musteri_kayıt/', views.musteri_register, name='musteri_kayıt'),
    path('admin_arac_sil/<int:arac_id>/', views.admin_arac_sil, name='admin_arac_sil'),
    path('admin_rezervasyon/', views.admin_rezervasyon_listesi, name='admin_rezervasyon'),
    path('arac_guncelle/<int:arac_id>/', views.arac_guncelle, name='arac_guncelle'),
    path('hakkımızda/', views.hakkımızda, name='hakkımızda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('odeme/<int:rezervasyon_id>/', views.odeme, name='odeme'),
    path('mevcut_rezervasyonlar/', views.mevcut_rezervasyonlar, name='mevcut_rezervasyonlar'),
    path('rezervasyon_guncelle/<int:rezervasyon_id>/', views.rezervasyon_guncelle, name='rezervasyon_guncelle'),
    path('rezervasyon_iptal/<int:rezervasyon_id>/', views.rezervasyon_iptal, name='rezervasyon_iptal'),
    path('admin_rezervasyon_guncelle/<int:rezervasyon_id>/', views.admin_rezervasyon_guncelle, name='admin_rezervasyon_guncelle'),
    path('admin_rezervasyon_iptal/<int:rezervasyon_id>/', views.admin_rezervasyon_iptal, name='admin_rezervasyon_iptal'),
    path('bilgilerimi_guncelle/', views.bilgilerimi_guncelle, name='bilgilerimi_guncelle'),
    path('dogrulama/', views.dogrulama, name='dogrulama'),
    path('admin_musteriler/', views.admin_musteriler, name='admin_musteriler'),  # Yeni URL
    path('musteri_sil/<int:musteri_id>/', views.musteri_sil, name='musteri_sil'),  # Yeni URL
    path('musteri_rezer/', views.musteri_rezer, name='musteri_rezer'),  # Yeni URL
    path('contact_view/', views.contact_view, name='contact_view'),
    path('sikayetler/', views.sikayetler_view, name='sikayetler'),
    path('sikayet_olustur/', views.sikayet_olustur, name='sikayet_olustur'),
    path('fiyat_filtrele/', views.fiyat_filtrele, name='fiyat_filtrele'),
    path('kontrol_rezervasyon/<int:arac_id>/', views.kontrol_rezervasyon, name='kontrol_rezervasyon'),
    path('ai_chat/', views.ai_chat, name='ai_chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
