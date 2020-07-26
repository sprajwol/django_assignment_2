from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from login_system.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture', 'current_address',
                  'primary_phone_number', 'secondary_phone_number')


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]
