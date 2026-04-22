from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')


def user_logout(request):
    logout(request)
    return redirect('/')