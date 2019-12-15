from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm, UserLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model


# Create your views here.
"""def welcome(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfully with username {username}')
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

    def home(request):
        return render(request, 'users/home.html')"""

def home(request):
    return render(request, 'users/home.html')

def login(request):
    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(user)
            return redirect('home')

    return render(request, 'users/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Welcome, You can now login to your account.')
            return redirect('login') 

    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form':form})
