from django.contrib import admin
from .models import Role, User, InventoryItem

admin.site.register(Role)
admin.site.register(User)
admin.site.register(InventoryItem)
