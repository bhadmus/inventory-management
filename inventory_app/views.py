from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegisterForm, InventoryForm, AuthenticationForm
from .models import InventoryItem


def register_view(request):
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


def user_login_view(request):
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


@login_required(login_url="login")
def user_logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def dashboard_view(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory_app/dashboard.html', {"items": items})


@login_required(login_url="login")
def inventory_view(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = InventoryForm()
    return render(request, 'inventory_app/inventory.html', {'form': form})


def index_view(request):
    # Implement your inventory logic here
    return render(request, 'inventory_app/index.html')
