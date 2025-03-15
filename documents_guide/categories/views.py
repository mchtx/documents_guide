from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AnaKategori, Kategori

class AnaKategoriListView(ListView):
    model = AnaKategori
    template_name = 'kategori/ana_kategori_list.html'
    context_object_name = 'ana_kategoriler'
    
    def get_queryset(self):
        return AnaKategori.objects.all()

class KategoriListView(ListView):
    model = Kategori
    template_name = 'kategori/kategori_list.html'
    context_object_name = 'kategoriler'

    def get_queryset(self):
        # Ana kategoriye göre kategorileri listele
        return Kategori.objects.filter(ana_kategori__slug=self.kwargs['slug'])

class KategoriDetailView(DetailView):
    model = Kategori
    template_name = 'kategori/kategori_detail.html'
    context_object_name = 'kategori'

    def get_object(self, queryset=None):
        return Kategori.objects.get(slug=self.kwargs['slug'])

# Create your views here.
