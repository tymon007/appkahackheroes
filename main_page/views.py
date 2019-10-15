from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Ciekawostki
import random

from .forms import SignUpForm


def main_page(request):
    ciekawostki = Ciekawostki.objects.all();
    randomowa_ciekawostka = random.choice(ciekawostki)
    return render(request, 'main_page/index.html', context={'randomowa_ciekawostka': randomowa_ciekawostka})


def log_in(request):
    return render(request, 'login.html')


def auth_login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main_page')
    else:
        return redirect('log_in')


def sign_in(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def credits(request):
    return render(request, 'credits.html')


def water(request):
    return render(request, 'water.html')




