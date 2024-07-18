from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    roles = models.ManyToManyField(Role)


class InventoryItem(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



