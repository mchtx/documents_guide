
from django.shortcuts import render
from .models import Document

def index(request):
    # Document modelinden tüm belgeleri al
    documents = Document.objects.all()
    
    # Frontend'e göndermek için context oluştur
    context = {
        'documents': documents,
    }
    
    # index.html'e verilerle birlikte render et
    return render(request, 'index.html', context)