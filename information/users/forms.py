from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = customUser
        fields = ['username', 'email', 'password1', 'password2']
# Compare this snippet from information/users/views.py:
