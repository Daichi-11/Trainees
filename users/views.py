from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib import messages


def user_signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')
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
            messages.success(request, 'Login successfully!')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def user_profile(request):
    return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        if user_profile:
            user_profile.delete()
            request.user.delete()
            logout(request)
            return redirect('users:login')

    return render(request, 'users/delete_profile.html')