from django.db import models
from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=200)  # Belge adı
    description = models.TextField()  # Açıklama
    image = models.ImageField(upload_to='documents/')  # Görsel
    steps = models.TextField()  # Belge alma adımları
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi

    def __str__(self):
        return self.name

# Create your models here.
