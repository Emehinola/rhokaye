from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm, UserLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/home.html')

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

def access(request):
    return render(request, 'users/access.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')
