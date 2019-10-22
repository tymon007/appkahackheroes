from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import User, Curiosity, Gas, Power, Water
import random
import re
from .forms import SignUpForm
from django.contrib.auth.models import User
import datetime


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
        form = SignUpForm(request.POST)

        username = request.POST['username']
        howManyPeople = request.POST['howManyPeople']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        username_valid = True
        for char in username:
            if char.isalpha() or char.isdigit():
                continue
            else:
                username_valid = False
                break

        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex, email):
            email_valid = True
        else:
            email_valid = False

        if password1 == "" and password2 == "":
            passwords_valid = False
        else:
            if password1 != password2:
                passwords_valid = False
            else:
                if len(password1) < 5:
                    passwords_valid = False
                else:
                    passwords_valid = True

        if username_valid and email_valid and passwords_valid:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('main_page')
            else:
                exeptions.append('Some errors detected: Form is invalid')
                # exeptions.append(['username: ' + username, 'howManyPeople: ' + howManyPeople, 'email: ' + email,
                #                  'password1: ' + password1, 'passwords2: ' + password2, username_valid, email_valid,
                #                   passwords_valid])
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


def gas_addValue(request):
    if request.method == 'POST':
        idOfUser = 100  # id of update

        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")  # date of update

        value = request.POST.get('value');  # value of update

        gas_instance = Gas.objects.create(idOfUser=idOfUser, date=date, value=value)
        return redirect('main_page')


def power(request):
    return render(request, 'environment/power.html')


def power_addValue(request):
    if request.method == 'POST':
        idOfUser = 100  # id of update

        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")  # date of update

        value = request.POST.get('value');  # value of update

        gas_instance = Power.objects.create(idOfUser=idOfUser, date=date, value=value)
        return redirect('main_page')


def water(request):
    return render(request, 'environment/water.html')


def water_addValue(request):
    if request.method == 'POST':
        idOfUser = 100  # id of update

        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")  # date of update

        value = request.POST.get('value');  # value of update

        gas_instance = Water.objects.create(idOfUser=idOfUser, date=date, value=value)
        return redirect('main_page')


def credits(request):
    return render(request, 'credits.html')
