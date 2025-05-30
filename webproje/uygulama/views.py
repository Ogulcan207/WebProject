from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import AracForm, MusteriForm
from .models import Arac, Musteri
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm, RezervasyonForm, AracForm,MusteriForm,ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from pyexpat.errors import messages
from django.contrib.auth.models import User



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

def hakkımızda(request):
    return render(request, 'hakkımızda.html')


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