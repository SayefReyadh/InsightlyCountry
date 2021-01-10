from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login, logout

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Has Been Created")
                return redirect('login')
            else:
                print("Not Valid")

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            user = request.POST.get('username')
            passw = request.POST.get('password')
            print(user, passw)
            user = authenticate(request, username=user, password=passw)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is Incorrect')
                return redirect('login')
        else:
            return render(request, 'accounts/login.html')


def logout_page(request):
    logout(request)
    return redirect('login')