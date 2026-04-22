from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect


# ================== ĐĂNG NHẬP ==================
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'accounts/login.html')


# ================== ĐĂNG KÝ ==================
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        # kiểm tra trùng username
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': 'Username đã tồn tại'
            })

        # tạo user
        user = User.objects.create_user(username=username, password=password)

        # đăng nhập luôn sau khi đăng ký
        login(request, user)

        return redirect('/')

    return render(request, 'accounts/register.html')


# ================== ĐĂNG XUẤT ==================
def user_logout(request):
    logout(request)
    return redirect('/')

   