from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *


def home(request):
    context = {'name': 'this is usama'}
    return render(request, context)


def dashboard(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home/')
                print("login ducesfull")
    context = {'forms': forms}
    return render(request, 'login.html', context)


@login_required(login_url='/')
def admin_logout(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        if password == password_repeat:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exist")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exist")
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                redirect('home/')
                messages.info(request, "Username creater")

        else:
            messages.info(request, "password not match")
    return render(request, 'register.html')
