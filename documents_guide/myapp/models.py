from django.contrib.auth.models import AbstractUser
from django.db import models

# Önce City ve District modellerini tanımlayın
class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')
    
    def __str__(self):
        return self.name

# Sonra CustomUser modelini tanımlayın
class CustomUser(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)  # null ve blank=True ekledim
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)  # null ve blank=True ekledim
    
    def __str__(self):
        return self.username

# Kurum Modeli
class Institution(models.Model):
    name = models.CharField(max_length=255)  # Kurum adı
    address = models.TextField()  # Kurum adresi
    phone = models.CharField(max_length=15)  # Telefon numarası
    email = models.EmailField()  # E-posta adresi
    website = models.URLField()  # Web sitesi
    city = models.ForeignKey(City, on_delete=models.CASCADE)  # Şehre bağlı kurum
    district = models.ForeignKey(District, on_delete=models.CASCADE)  # İlçeye bağlı kurum

    def __str__(self):
        return self.name

# İşlem Modeli
class Process(models.Model):
    name = models.CharField(max_length=255)  # İşlem adı
    description = models.TextField()  # İşlem açıklaması
    steps = models.TextField()  # Adım adım açıklamalar
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='processes')  # Şehre bağlı işlem
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='processes')  # İlçeye bağlı işlem

    def __str__(self):
        return self.name

