from django import forms
from .models import Arac,Rezervasyon,Musteri,ContactMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AracForm(forms.ModelForm):
    class Meta:
        model = Arac
        fields = ['marka', 'model', 'yil', 'fiyat', 'resim']  # Resim alanını ekleyin

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı')
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class RezervasyonForm(forms.ModelForm):
    baslangic_tarihi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    bitis_tarihi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Rezervasyon
        fields = ['baslangic_tarihi', 'bitis_tarihi']

class MusteriForm(forms.ModelForm):
    class Meta:
        model = Musteri
        fields = ['ad', 'soyad', 'tc', 'kullanici_adi', 'sifre','email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class VerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, label='Doğrulama Kodu')