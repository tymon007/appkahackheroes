from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Curiosity
import random

from .forms import SignUpForm


def main_page(request):
    curiosities = Curiosity.objects.all()
    random_curiosity = random.choice(curiosities)
    return render(request, 'main_page/index.html', context={'random_curiosity': random_curiosity})


def log_in(request):
    return render(request, 'registration/login.html')


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
    return render(request, 'registration/signup.html')


def auth_signin(request):
    exeptions = [];

    if request.method == 'POST':
        exeptions.append('Success: Method is POST')
        form = SignUpForm(request.POST)
        if form.is_valid():
            exeptions[1] = 'Success: Form is valid';
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
        else:
            exeptions.append('Some errors detected: Form is invalid')
            exeptions.append(form)
    else:
        exeptions.append('Some errors detected: Method is not POST')
    return render(request, 'registration/signup.html', {'exeptions': exeptions})


def me(request):
    return render(request, 'aboutMe/me.html')


def timer(request):
    return render(request, 'aboutMe/timer.html')


def food(request):
    return render(request, 'environment/food.html')


def gas(request):
    return render(request, 'environment/gas.html')


def power(request):
    return render(request, 'environment/power.html')


def water(request):
    return render(request, 'environment/water.html')


def credits(request):
    return render(request, 'credits.html')
