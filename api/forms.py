from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importa User desde django.contrib.auth.models
from .models import Profile
from django import forms

class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')
