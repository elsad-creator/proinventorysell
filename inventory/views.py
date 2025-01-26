from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product

# Seçilmiş 5 istifadəçi və şifrələri
ALLOWED_USERNAMES = {"Admin2", "user2", "user3", "user4", "user5"}

def home(request):
    return render(request, 'inventory/home.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # İstifadəçi adı icazə verilənlərdən deyilsə
        if username not in ALLOWED_USERNAMES:
            messages.error(request, 'Bu istifadəçi adı ilə giriş icazəsi yoxdur!')
            return render(request, 'inventory/sign_in.html')

        # Django-nun daxili sistemində yoxlama
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'İstifadəçi adı və ya şifrə yanlışdır!')
    return render(request, 'inventory/sign_in.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        product_name = request.POST.get('product_name')
        date_added = request.POST.get('date_added')

        # Yeni məhsul yaradın
        Product.objects.create(
            serial_number=serial_number,
            product_name=product_name,
            date_added=date_added,
            added_by=request.user
        )
        messages.success(request, 'Məhsul uğurla əlavə edildi!')
        return redirect('dashboard')
    return render(request, 'inventory/dashboard.html')