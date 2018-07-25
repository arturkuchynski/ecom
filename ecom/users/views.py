from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.db import transaction
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import *


@login_required(login_url='users:user_login')
def info(request):
    print(get_token(request))
    cart = Cart(request)
    user = request.user
    return render(request, 'info.html', {'cart': cart, 'user': user})


@csrf_protect
def user_login(request):
    print(get_token(request))
    cart = Cart(request)
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to a success page.
            messages.success(request, 'You have been logged in successfully')
            return redirect('users:info')
        else:
            # return an 'invalid login or password' error message.
            messages.success(request, 'Error logging in, please try again')
            return redirect('users:user_login')

    else:
        return render(request, 'login.html', {'cart': cart})


@csrf_protect
def user_logout(request):
    print(get_token(request))
    logout(request)
    update_session_auth_hash(request, request.user)
    messages.success(request, 'You have been logged out')
    return redirect('bookstore:book_list')


def user_register(request):
    print(get_token(request))
    cart = Cart(request)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered')
            return redirect('users:info')
    else:
        form = RegisterForm()

    context = {'form': form, 'cart': cart}
    return render(request, 'register.html', context)

@csrf_protect
@login_required(login_url='users:user_login')
@transaction.atomic
def edit_profile(request):
    cart = Cart(request)
    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # autofill data
            # form.username = form['username'].value() + form['username'].value()

            messages.success(request, 'You have edited your profile')
            return redirect('users:info')

    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

    forms = user_form, profile_form

    context = {'forms': forms,
               'cart': cart}

    return render(request, 'edit.html', context)


@csrf_protect
@login_required(login_url='users:user_login')
def change_password(request):
    print(get_token(request))
    cart = Cart(request)
    if request.method == "POST":
        form = ChangeUserPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # update hash to stay logged in
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have edited your password')
            return redirect('users:info')
    else:
        form = ChangeUserPasswordForm(user=request.user)

    context = {'form': form, 'cart': cart}
    return render(request, 'change_password.html', context)
