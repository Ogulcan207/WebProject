from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from MySQLdb import IntegrityError
from .forms import AracForm, MusteriForm, ContactForm, RezervasyonForm, VerificationForm, Rezervasyon
from .models import Arac, Musteri
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from pyexpat.errors import messages
from django.contrib import messages  # Import the messages module
from .utils import generate_verification_code, send_verification_email

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

def iletisim(request):
    return render(request, 'iletisim.html')


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
