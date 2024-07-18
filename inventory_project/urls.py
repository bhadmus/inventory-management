from django.contrib import admin
from django.urls import path, include
from inventory_app import views as inventory_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', inventory_views.register, name='register'),
    path('login/', inventory_views.user_login, name='login'),
    path('logout/', inventory_views.user_logout, name='logout'),
    path('dashboard/', inventory_views.dashboard, name='dashboard'),
    path('inventory/', inventory_views.inventory, name='inventory'),
    path('', inventory_views.dashboard, name='home'),
]
