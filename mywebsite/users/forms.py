
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Django's built-in User
from .models import Profile
class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Uses Django's built-in User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Uses Django's built-in User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =['image']