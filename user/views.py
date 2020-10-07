from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *


def home(request):
    context = {'name': 'this is usama'}
    return render(request, context)

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
        Username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        user = User.objects.create_user(username=Username, email=email, password=password,first_name=first_name,last_name=last_name)
        user.save()
        redirect('home/')
        print('object created')
    return render(request, 'register.html')
