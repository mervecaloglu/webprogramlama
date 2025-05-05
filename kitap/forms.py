from django import forms

class KitapFiltreForm(forms.Form):
    baslik = forms.CharField(label='Başlıkta Ara', max_length=100, required=False)
    icerik = forms.CharField(label='İçerikte Ara', max_length=100, required=False)
    min_fiyat = forms.DecimalField(label='Minimum Fiyat', required=False)
    max_fiyat = forms.DecimalField(label='Maksimum Fiyat', required=False)
    baslangic_tarihi = forms.DateField(label='Başlangıç Tarihi', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    bitis_tarihi = forms.DateField(label='Bitiş Tarihi', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
