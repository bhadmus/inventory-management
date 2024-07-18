from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegisterForm, InventoryForm, AuthenticationForm
from .models import InventoryItem


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'inventory_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'inventory_app/dashboard.html')


@login_required
def inventory(request):
    items = InventoryItem.objects.all()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = InventoryForm()
    return render(request, 'inventory_app/inventory.html', {'form': form, 'items': items})


def register_view(request):
    # Implement your register logic here
    return render(request, 'inventory_app/register.html')


def login_view(request):
    # Implement your login logic here
    return render(request, 'inventory_app/login.html')


def logout_view(request):
    # Implement your logout logic here
    return render(request, 'inventory_app/logout.html')


def dashboard_view(request):
    # Implement your dashboard logic here
    return render(request, 'inventory_app/dashboard.html')


def inventory_view(request):
    # Implement your inventory logic here
    return render(request, 'inventory_app/inventory.html')
