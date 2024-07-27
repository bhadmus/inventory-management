from django.contrib import admin
from django.urls import path, include
# from inventory_app import views as inventory_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("inventory_app.urls"))
]
