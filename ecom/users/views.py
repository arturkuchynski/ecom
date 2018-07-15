from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to a success page.
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            # return an 'invalid login or password' error message.
            messages.success(request, 'Error logging in, please try again')
            return redirect('user_login')

    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def user_register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered')
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # autofill data
            # form.username = form['username'].value() + form['username'].value()
            form.save()
            messages.success(request, 'You have edited your profile')
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'edit.html', context)


def change_password(request):
    if request.method == "POST":
        form = ChangeUserPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # update hash to stay logged in
            update_session_auth_hash(request,form.user)
            messages.success(request, 'You have edited your password')
            return redirect('home')
    else:
        form = ChangeUserPasswordForm(user=request.user)

    context = {'form': form}
    return render(request, 'change_password.html', context)