from django.db import models
from django.urls import reverse

class AnaKategori(models.Model):
    # Ana Kategori modelini tanımlar
    ad = models.CharField(max_length=255, unique=True)  # Kategorinin adını tanımlar (benzersiz)
    slug = models.SlugField(unique=True)  # SEO dostu URL oluşturmak için, her ana kategoriye özel slug
    açıklama = models.TextField(blank=True, null=True)  # Opsiyonel açıklama alanı
    
    class Meta:
        ordering = ['ad']  # Ana kategoriler alfabetik olarak sıralanır
        verbose_name = 'Ana Kategori'  # Django Admin için adlandırma
        verbose_name_plural = 'Ana Kategoriler'  # Django Admin için çoğul adlandırma
    
    def __str__(self):
        return self.ad  # Modelin string gösterimi, kategori adını döndürür

    def get_absolute_url(self):
        # Ana kategori detayına gidilecek URL'yi döndüren fonksiyon
        return reverse('kategori_list', kwargs={'slug': self.slug})


class Kategori(models.Model):
    # Kategori modelini tanımlar
    ad = models.CharField(max_length=255)  # Kategori adı
    slug = models.SlugField(unique=True)  # SEO dostu URL için her kategoriye özel slug
    açıklama = models.TextField(blank=True, null=True)  # Opsiyonel açıklama alanı
    ana_kategori = models.ForeignKey(AnaKategori, on_delete=models.CASCADE, related_name="kategoriler")  
    # Her kategori bir ana kategoriye ait olur. ForeignKey ile AnaKategori'ye bağlanır

    class Meta:
        ordering = ['ad']  # Kategoriler alfabetik olarak sıralanır
        verbose_name = 'Kategori'  # Django Admin için kategori adı
        verbose_name_plural = 'Kategoriler'  # Django Admin için kategorilerin çoğul adı
        constraints = [
            # Aynı adla birden fazla kategori olmasını engellemek için unique constraint
            models.UniqueConstraint(fields=['ad', 'ana_kategori'], name='unique_kategori_ad_ana_kategori')
        ]
    
    def __str__(self):
        return self.ad  # Modelin string gösterimi, kategori adını döndürür

    def get_absolute_url(self):
        # Kategori detayına gidilecek URL'yi döndüren fonksiyon
        return reverse('kategori_detail', kwargs={'slug': self.slug})























