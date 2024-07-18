from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm as DjangoAuthenticationForm
from .models import User, InventoryItem


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthenticationForm(DjangoAuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'quantity', 'price']
