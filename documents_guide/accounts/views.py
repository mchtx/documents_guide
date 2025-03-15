from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileCreationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            userprofile = form.save()
            login(request, userprofile.user)  # Kullanıcıyı giriş yapmış olarak ayarla
            return redirect('home')
    else:
        form = UserProfileCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Başarılı giriş sonrası yönlendirme
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
