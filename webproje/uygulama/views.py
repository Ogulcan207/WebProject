from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from MySQLdb import IntegrityError
from .forms import AracForm, MusteriForm, ContactForm, RezervasyonForm, VerificationForm, Rezervasyon
from .models import Arac, Musteri, Rezervasyon, ContactMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, RezervasyonForm, AracForm,MusteriForm,ContactForm, VerificationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.contrib import messages  # Import the messages module
from .utils import generate_verification_code, send_verification_email
from django.core.mail import send_mail
from datetime import timezone
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db import connection
import random, string

def anasayfa(request):
    return render(request, 'anasayfa.html')

@login_required
def admin_arac_liste(request):
    if not request.user.is_staff:
        return redirect('login')
    
    araclar_list = Arac.objects.all()
    
    paginator = Paginator(araclar_list, 2)  # 2 araç per sayfa
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = AracForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_arac_liste')
    else:
        form = AracForm()
    
    return render(request, 'admin_arac_liste.html', {'araclar': page_obj, 'form': form})

def arac_listesi(request):
    araclar_list = Arac.objects.all()
    paginator = Paginator(araclar_list, 3)  # Sayfa başına 6 araç
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'arac_listesi.html', {'page_obj': page_obj})

def arac_ekle(request):
    if request.method == 'POST':
        form = AracForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('arac_listesi')
    else:
        form = AracForm()
    return render(request, 'arac_ekle.html', {'form': form})

def arac_sil(request, arac_id):
    arac = get_object_or_404(Arac, id=arac_id)
    if request.method == 'POST':
        arac.delete()
        return redirect('arac_listesi')
    return render(request, 'arac_sil.html', {'arac': arac})

@login_required
def admin_arac_sil(request, arac_id):
    arac = get_object_or_404(Arac, id=arac_id)
    if request.method == 'POST':
        arac.delete()
        return redirect('admin_arac_liste')
    return render(request, 'admin_arac_liste.html', {'arac': arac})

@login_required
def admin_paneli(request):
    if request.session.get('user_type') != 'admin':
        return redirect('login')
    araclar = Arac.objects.all()
    return render(request, 'admin_paneli.html', {'araclar': araclar})

@login_required
def arac_guncelle(request, arac_id):
    arac = get_object_or_404(Arac, id=arac_id)
    if request.method == 'POST':
        form = AracForm(request.POST, request.FILES, instance=arac)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_arac_liste'))
    else:
        form = AracForm(instance=arac)
    
    return render(request, 'arac_guncelle.html', {'form': form})

@login_required
def admin_musteriler(request):
    musteriler = Musteri.objects.all()
    paginator = Paginator(musteriler, 1)  # Sayfa başına 6 araç
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_musteriler.html', {'page_obj': page_obj})

@login_required
def musteri_sil(request, musteri_id):
    musteri = get_object_or_404(Musteri, id=musteri_id)
    musteri.delete()
    return redirect('admin_musteriler')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    request.session['user_type'] = 'admin'  # Kullanıcı türünü oturumda sakla
                    return redirect('admin_paneli')
                else:
                    request.session['user_type'] = 'musteri'  # Kullanıcı türünü oturumda sakla
                    return redirect('musteri_paneli')
            else:
                form.add_error(None, 'Kullanıcı adı veya şifre yanlış')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    request.session.flush()
    return redirect('anasayfa')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Admin olarak kaydetmek için is_superuser ve is_staff alanlarını True yapıyoruz
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def musteri_logout(request):
    logout(request)
    request.session.flush()
    return redirect('anasayfa')

def musteri_register(request):
    if request.method == 'POST':
        form = MusteriForm(request.POST, request.FILES)
        if form.is_valid():
            # Kullanıcı adı benzersiz mi kontrol et
            username = form.cleaned_data.get('kullanici_adi')
            password = form.cleaned_data.get('sifre')
            email = form.cleaned_data.get('email')  # E-posta alanını al
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu kullanıcı adı zaten alınmış.')
            else:
                # Yeni kullanıcı oluştur
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                form.instance.user = user  # Musteri modelinde user alanı varsa
                form.save()  # Form verilerini doğrudan Musteri modeline kaydediyoruz
                return redirect('musteri_paneli')  # Başka bir sayfaya yönlendirme yapabilirsiniz
    else:
        form = MusteriForm()
    
    return render(request, 'musteri_kayıt.html', {'form': form})

@login_required
def rezervasyon(request, arac_id):
    arac = get_object_or_404(Arac, id=arac_id)
    
    # Session'dan tarihleri al
    start_date = request.session.get('start_date')
    end_date = request.session.get('end_date')
    
    if request.method == 'POST':
        form = RezervasyonForm(request.POST)
        if form.is_valid():
            try:
                musteri = Musteri.objects.get(kullanici_adi=request.user.username)
                rezervasyon = form.save(commit=False)
                rezervasyon.musteri = musteri
                rezervasyon.arac = arac
                
                start_date = form.cleaned_data['baslangic_tarihi']
                end_date = form.cleaned_data['bitis_tarihi']
                
                # Tarih kontrolü
                existing_rezervasyonlar = Rezervasyon.objects.filter(
                    arac=arac,
                    baslangic_tarihi__lt=end_date,
                    bitis_tarihi__gt=start_date
                )
                if existing_rezervasyonlar.exists():
                    messages.error(request, 'Seçtiğiniz tarihler arasında bu araç zaten rezerve edilmiştir.')
                else:
                    time_diff = abs((end_date - start_date).days)
                    total_price = time_diff * arac.fiyat
                    
                    rezervasyon.save()
                    
                    request.session['rezervasyon_id'] = rezervasyon.id
                    request.session['total_price'] = float(total_price)
                    return redirect('odeme', rezervasyon_id=rezervasyon.id)
            except Musteri.DoesNotExist:
                messages.error(request, 'Müşteri bulunamadı.')
            except IntegrityError as e:
                messages.error(request, f'Bir hata oluştu: {e}')
            except Exception as e:
                messages.error(request, f'Beklenmeyen bir hata oluştu: {e}')
                print(f'Beklenmeyen bir hata oluştu: {e}')
        else:
            print(form.errors)
    else:
        initial_data = {}
        if start_date:
            initial_data['baslangic_tarihi'] = start_date
        if end_date:
            initial_data['bitis_tarihi'] = end_date
        form = RezervasyonForm(initial=initial_data)
    
    return render(request, 'rezervasyon.html', {'form': form, 'arac': arac, 'start_date': start_date, 'end_date': end_date})

@csrf_exempt
@login_required
def odeme(request, rezervasyon_id):
    if request.method == 'POST':
        # Ödeme işlemlerini burada gerçekleştirin
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        
        # Ödeme işlemi başarılıysa
        rezervasyon = get_object_or_404(Rezervasyon, id=rezervasyon_id)
        rezervasyon.save()
        
        # Doğrulama kodunu oluştur ve e-posta gönder
        musteri = Musteri.objects.get(kullanici_adi=request.user.username)
        email = musteri.email
        verification_code = generate_verification_code()
        request.session['verification_code'] = verification_code
        send_verification_email(email, verification_code)
        
        # Oturumdan rezervasyon bilgilerini temizleyin
        del request.session['rezervasyon_id']
        del request.session['total_price']
        
        return redirect('dogrulama')  # Doğrulama sayfasına yönlendir
    total_price = request.session.get('total_price', 0)
    return render(request, 'odeme.html', {'total_price': total_price})

@login_required
def dogrulama(request):
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verification_code']
            if entered_code == request.session.get('verification_code'):
                # Ödeme işlemini tamamlayın ve mevcut rezervasyonlar sayfasına yönlendirin
                return redirect('mevcut_rezervasyonlar')
            else:
                form.add_error('verification_code', 'Doğrulama kodu yanlış.')
    else:
        form = VerificationForm()
    return render(request, 'dogrulama.html', {'form': form})

@login_required
def rezervasyon_iptal(request, rezervasyon_id):
    rezervasyon = get_object_or_404(Rezervasyon, id=rezervasyon_id, musteri__kullanici_adi=request.user.username)
    if request.method == 'POST':
        rezervasyon.delete()
        return redirect('mevcut_rezervasyonlar')
    return render(request, 'rezervasyon_iptal.html', {'rezervasyon': rezervasyon})

def is_admin(user):
    return user.is_superuser

def musteri_login(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('kullanici_adi')
        sifre = request.POST.get('sifre')
        
        # Kullanıcıyı doğrula
        user = authenticate(request, username=kullanici_adi, password=sifre)
        
        if user is not None and not user.is_superuser:  # Check if user is not a superuser
            login(request, user)
            request.session['user_type'] = 'musteri'  # Kullanıcı türünü oturumda sakla
            
            # Hedef URL'yi kontrol et ve yönlendir
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('musteri_paneli')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış.')
            print(f"Giriş denemesi: Kullanıcı adı: {kullanici_adi}, Şifre: {sifre}")  # Hata ayıklama için
    return render(request, 'musteri_login.html')

def musteri_rezer(request):
    araclar_list = Arac.objects.all()
    paginator = Paginator(araclar_list, 3)  # Sayfa başına 6 araç
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'musteri_rezer.html', {'page_obj': page_obj})

@login_required
def admin_rezervasyon_listesi(request):

    if not request.user.is_staff:
        return redirect('login')
    
    rezervasyonlar = Rezervasyon.objects.all()
    paginator = Paginator(rezervasyonlar, 2)  # Sayfa başına 6 araç
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_rezervasyon.html', {'page_obj': page_obj})

@login_required
@user_passes_test(is_admin)
def admin_rezervasyon_guncelle(request, rezervasyon_id):
    rezervasyon = get_object_or_404(Rezervasyon, id=rezervasyon_id)
    if request.method == 'POST':
        form = RezervasyonForm(request.POST, instance=rezervasyon)
        if form.is_valid():
            form.save()
            return redirect('admin_rezervasyon')
    else:
        form = RezervasyonForm(instance=rezervasyon)
    return render(request, 'rezervasyon_guncelle.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def admin_rezervasyon_iptal(request, rezervasyon_id):
    rezervasyon = get_object_or_404(Rezervasyon, id=rezervasyon_id)
    if request.method == 'POST':
        rezervasyon.delete()
        return redirect('admin_rezervasyon')
    return render(request, 'rezervasyon_iptal.html', {'rezervasyon': rezervasyon})

@login_required
def bilgilerimi_guncelle(request):
    musteri = Musteri.objects.get(kullanici_adi=request.user.username)
    if request.method == 'POST':
        form = MusteriForm(request.POST, instance=musteri)
        if form.is_valid():
            form.save()
            return redirect('musteri_paneli')
    else:
        form = MusteriForm(instance=musteri)
    return render(request, 'bilgilerimi_guncelle.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_view')  # Başarılı iletişim sayfasına yönlendirme yapılabilir
        else:
            # Form geçersiz olduğunda hata mesajlarını görmek için form hatalarını ekrana yazdırın
            print(form.errors)
    else:
        form = ContactForm()
    
    return render(request, 'iletisim.html', {'form': form})

@login_required
def mevcut_rezervasyonlar(request):
    musteri = get_object_or_404(Musteri, kullanici_adi=request.user.username)
    rezervasyonlar_list = Rezervasyon.objects.filter(musteri=musteri, bitis_tarihi__gte=timezone.now())
    paginator = Paginator(rezervasyonlar_list, 1)  # Sayfa başına 10 rezervasyon
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mevcut_rezervasyonlar.html', {
        'page_obj': page_obj
    })

@login_required
def musteri_paneli(request):
    if request.session.get('user_type') != 'musteri':
        return redirect('musteri_login')
    araclar = Arac.objects.all()
    return render(request, 'musteri_paneli.html', {'araclar': araclar})

def fiyat_filtrele(request):
    if request.method == 'POST':
        min_price = request.POST.get('minPrice')
        max_price = request.POST.get('maxPrice')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')

        # Fiyat aralığına göre araçları filtrele
        filtered_cars = Arac.objects.all()
        if min_price:
            filtered_cars = filtered_cars.filter(fiyat__gte=min_price)
        if max_price:
            filtered_cars = filtered_cars.filter(fiyat__lte=max_price)

        # Tarih aralığına göre araçları filtrele
        if start_date and end_date:
            # Belirtilen tarih aralığında rezervasyonu olmayan araçları filtrele
            filtered_cars = filtered_cars.exclude(
                Q(rezervasyon__baslangic_tarihi__lt=end_date) & Q(rezervasyon__bitis_tarihi__gt=start_date)
            )

        # Tarihleri session'a kaydet
        request.session['start_date'] = start_date
        request.session['end_date'] = end_date

        context = {
            'filtered_cars': filtered_cars,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render(request, 'fiyat_filtrele.html', context)
    else:
        return render(request, 'anasayfa.html')
    
@login_required
def rezervasyon_guncelle(request, rezervasyon_id):
    rezervasyon = get_object_or_404(Rezervasyon, id=rezervasyon_id, musteri__kullanici_adi=request.user.username)
    if request.method == 'POST':
        form = RezervasyonForm(request.POST, instance=rezervasyon)
        if form.is_valid():
            form.save()
            return redirect('mevcut_rezervasyonlar')
    else:
        form = RezervasyonForm(instance=rezervasyon)
    return render(request, 'rezervasyon_guncelle.html', {'form': form})

def kontrol_rezervasyon(request, arac_id):
    baslangic_tarihi = request.GET.get('baslangic_tarihi')
    bitis_tarihi = request.GET.get('bitis_tarihi')
    rezervasyonlar = Rezervasyon.objects.filter(
        arac_id=arac_id,
        baslangic_tarihi__lt=bitis_tarihi,
        bitis_tarihi__gt=baslangic_tarihi
    )
    return JsonResponse({'rezervasyonlar': list(rezervasyonlar.values())})

def sikayetler_view(request):
    complaints = ContactMessage.objects.all().order_by('-created_at')  # Assuming ContactMessage is the model for complaints
    paginator = Paginator(complaints, 2)  # Show 10 complaints per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sikayetler.html', {'complaints': page_obj})

def sikayet_olustur(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                musteri = Musteri.objects.get(kullanici_adi=request.user.username)
                form.instance.name = musteri.ad  # Musteri modelinden adı al
                form.instance.email = musteri.email  # Musteri modelinden e-posta adresini al
                form.save()
                return redirect('musteri_paneli')
            else:
                return redirect('login')
    else:
        musteri = Musteri.objects.get(kullanici_adi=request.user.username)
        initial_data = {'name': musteri.ad, 'email': musteri.email}
        form = ContactForm(initial=initial_data)
    
    return render(request, 'sikayet_olustur.html', {'form': form, 'musteri': musteri})

def iletisim(request):
    return render(request, 'iletisim.html')

def hakkımızda(request):
    return render(request, 'hakkımızda.html')