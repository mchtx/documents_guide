from django.urls import path
from . import views

urlpatterns = [
    # Ana Kategoriler listesi
    path('', views.AnaKategoriListView.as_view(), name='ana_kategori_list'),

    # Her bir Ana Kategorinin altındaki Kategoriler
    path('kategori/<slug:slug>/', views.KategoriListView.as_view(), name='kategori_list'),

    # Kategori detay sayfası
    path('kategori/<slug:slug>/detay/', views.KategoriDetailView.as_view(), name='kategori_detail'),  # Detay için yeni URL
]
