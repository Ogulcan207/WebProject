from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import AracForm, MusteriForm
from .models import Arac, Musteri
from django.contrib.auth.decorators import login_required
from django.urls import reverse



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

def admin_arac_sil(request, arac_id):
    arac = get_object_or_404(Arac, id=arac_id)
    if request.method == 'POST':
        arac.delete()
        return redirect('admin_arac_liste')
    return render(request, 'admin_arac_liste.html', {'arac': arac})


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