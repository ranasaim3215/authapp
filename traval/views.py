from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Team
from .forms import *
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
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'login.html', context)
def home(request):
    team=Team.objects.all()
    context={'team': team,}
    return render(request, 'table.html',context)

