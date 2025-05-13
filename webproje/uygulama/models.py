from django.db import models

class Arac(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    yil = models.IntegerField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    resim = models.ImageField(upload_to='arac_resimleri/', blank=True, null=True)  # Resim alanı

    def __str__(self):
        return f"{self.marka} {self.model} ({self.yil})"

class Musteri(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    tc = models.IntegerField()
    kullanici_adi = models.CharField(max_length=50)
    sifre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)  # Yeni email alanı

    def __str__(self):
        return f"{self.ad} {self.soyad}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
           
class Rezervasyon(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    arac = models.ForeignKey(Arac, on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        self.fiyat = self.calculate_price()
        super().save(*args, **kwargs)

    def calculate_price(self):
        gun_sayisi = (self.bitis_tarihi - self.baslangic_tarihi).days
        gunluk_ucret = self.arac.fiyat  # Araç fiyatını kullan
        return gun_sayisi * gunluk_ucret

    def __str__(self):
        return f"{self.musteri} - {self.arac} ({self.baslangic_tarihi} - {self.bitis_tarihi})"