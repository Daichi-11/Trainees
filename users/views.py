from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('home')  
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')