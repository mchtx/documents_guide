from django.contrib import admin
from .models import AnaKategori, Kategori

class KategoriInline(admin.TabularInline):
    model = Kategori
    extra = 1  # Yeni kategori eklemek için 1 boş satır bırakır

class AnaKategoriAdmin(admin.ModelAdmin):
    list_display = ['ad', 'slug', 'açıklama']
    search_fields = ['ad']
    inlines = [KategoriInline]

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['ad', 'slug', 'ana_kategori']
    search_fields = ['ad', 'ana_kategori__ad']
    list_filter = ['ana_kategori']

admin.site.register(AnaKategori, AnaKategoriAdmin)
admin.site.register(Kategori, KategoriAdmin)
