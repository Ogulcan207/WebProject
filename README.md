# WebProject - Araç Kiralama Sistemi

Bu proje, Django 5.1.7 ve Python 3.11.0 kullanılarak geliştirilmiş, Docker destekli bir **araç kiralama platformudur**.

---

## 🔍 Proje Özeti

Bu projede bir araç kiralama sisteminin web tabanlı versiyonu geliştirilecektir. Django altyapısı kullanılarak hem müşterilere hem yöneticilere yönelik iki farklı panel oluşturulacaktır. Müşteriler sisteme kayıt olup araçları görüntüleyebilecek, tarih ve fiyat aralığına göre filtreleme yaparak rezervasyon oluşturabilecektir. Ödeme süreci sonrası doğrulama mekanizması uygulanacaktır. Yönetici tarafında araç, müşteri ve rezervasyon işlemleri kontrol edilecektir. Her ekip üyesi belirli bir özelliği kendi `feature` branch'inde geliştirecek, haftalık olarak `pull request` açarak projeye katkı sağlayacaktır. Projenin kurulumu ve çalıştırılması **Docker Compose** kullanılarak gerçekleştirilecektir.

---

## 🧑‍💻 Ekip Bilgisi

**Ekip Lideri:**  
220201152 / Oğulcan Alınlı / 220201152@kocaeli.edu.tr

**Github Deposu:**  
🔗 https://github.com/Ogulcan207/WebProject

---

## 🚀 Özellikler

- Kullanıcı kayıt ve giriş sistemi
- Admin paneli ile araç ve rezervasyon yönetimi
- Müşteri paneli ile rezervasyon ve bilgi güncelleme
- Araç filtreleme (fiyat / tarih)
- AI destekli araç öneri asistanı (Together.ai entegrasyonu)
- Bootstrap ile responsive arayüz
- Görsel yükleme desteği
- CSRF ve güvenlik kontrolleri
- Docker ile kolay kurulum

## Geliştiriciler

| No | Özellik                    | Sorumlu (Ad / No)          | Branch              | Açıklama                               |
| -- | -------------------------- | -------------------------- | ------------------- | -------------------------------------- |
| 1  | ORM / Migrations           | Yiğit Dikbaş (220201057)   | `feature-orm`       | models.py yapısı, migrate              |
| 2  | Web Servis                 | Yiğit Dikbaş               | `feature-api`       | JsonResponse + endpoint                |
| 3  | OOP Katmanı                | Ömer Şimşek (220201041)    | `feature-oop`       | Model, form, view OOP                  |
| 4  | Yetki Kontrolü (RBAC)      | Ömer Şimşek                | `feature-rbac`      | `@user_passes_test`                    |
| 5  | Yetkilendirme (Login/Auth) | Ubeydullah Gür (220201039) | `feature-auth`      | login / logout / auth                  |
| 6  | Session / Cookie Yönetimi  | Ubeydullah Gür             | `feature-session`   | `request.session` kullanımı            |
| 7  | Web Güvenlik               | Adem Alperen Arda          | `feature-security`  | CSRF, `@login_required`                |
| 8  | 3. Parti Kütüphaneler      | Adem Alperen Arda          | `feature-extension` | `ImageField`, `Paginator`, `send_mail` |
| 9  | Sunum Katmanı (UI)         | Oğulcan Alınlı (220201152) | `feature-ui`        | Bootstrap ile responsive arayüz        |
| 10 | AI Destekli Araç Asistanı  | Oğulcan Alınlı             | `feature-ai`        | Together.ai entegrasyonu               |

---

## 🔧 Teknolojiler

- Python 3.11.0
- Django 5.1.7
- MySQL 8.0
- Bootstrap 4.5
- Docker & Docker Compose

---

Geliştirici Modu (Docker Olmadan)

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 🐳 Docker ile Kurulum

```bash
# Gerekli dosyaları klonlayın
git clone https://github.com/Ogulcan207/WebProject
cd WebProject

# Uygulamayı başlatın
docker-compose up --build

Tarayıcıdan erişim:
🌐 http://localhost:8000