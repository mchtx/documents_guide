from django.shortcuts import render
from .models import Process, Institution, District, City, CustomUser

def index(request):
    # Tüm modellerden verileri al
    processes = Process.objects.all()
    institutions = Institution.objects.all()
    districts = District.objects.all()
    cities = City.objects.all()
    users = CustomUser.objects.all()

    # Frontend'e göndermek için context oluştur
    context = {
        'processes': processes,
        'institutions': institutions,
        'districts': districts,
        'cities': cities,
        'users': users,
    }

    # index.html'e verilerle birlikte render et
    return render(request, 'index.html', context)