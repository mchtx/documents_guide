from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')  # Gösterilecek alanlar
    search_fields = ('name', 'description')  # Arama yapılacak alanlar
    list_filter = ('created_at',)  # Filtreleme yapılacak alanlar
    ordering = ('-created_at',)  # Listeleme sırası

admin.site.register(Document, DocumentAdmin)





# Register your models here.
