from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Kitap, Yorum
from .forms import KitapFiltreForm, YorumForm

def kitap_listesi(request):
    form = KitapFiltreForm(request.GET or None)
    kitaplar = Kitap.objects.all()

    if form.is_valid():
        baslik = form.cleaned_data.get('baslik')
        icerik = form.cleaned_data.get('icerik')
        min_fiyat = form.cleaned_data.get('min_fiyat')
        max_fiyat = form.cleaned_data.get('max_fiyat')
        baslangic_tarihi = form.cleaned_data.get('baslangic_tarihi')
        bitis_tarihi = form.cleaned_data.get('bitis_tarihi')

        if baslik:
            kitaplar = kitaplar.filter(title__icontains=baslik)
        
        if icerik:
            kitaplar = kitaplar.filter(content__icontains=icerik)
        
        if min_fiyat is not None:
            kitaplar = kitaplar.filter(price__gte=min_fiyat)
        
        if max_fiyat is not None:
            kitaplar = kitaplar.filter(price__lte=max_fiyat)
        
        if baslangic_tarihi:
            kitaplar = kitaplar.filter(published_time__gte=baslangic_tarihi)
        
        if bitis_tarihi:
            kitaplar = kitaplar.filter(published_time__lte=bitis_tarihi)

    kitap_sayisi = kitaplar.count()

    return render(
        request,
        'kitap/kitap_listesi.html',
        {
            'kitaplar': kitaplar,
            'form': form,
            'kitap_sayisi': kitap_sayisi
        }
    )

def kitap_detay(request, pk):
    kitap = get_object_or_404(Kitap, pk=pk)
    yorumlar = kitap.yorumlar.all().order_by('-tarih')

    if request.method == 'POST':
        form = YorumForm(request.POST)
        if form.is_valid():
            yeni_yorum = form.save(commit=False)
            yeni_yorum.kitap = kitap
            yeni_yorum.save()
            return redirect('kitap_detay', pk=kitap.pk)
    else:
        form = YorumForm()

    return render(request, 'kitap/kitap_detay.html', {
        'kitap': kitap,
        'yorumlar': yorumlar,
        'form': form
    })
