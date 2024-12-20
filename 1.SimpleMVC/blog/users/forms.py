from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
    def __str__(self):
        # Example: returning the username if present or a generic message
        username = self.cleaned_data.get('username', 'CustomUserForm instance')
        first_name = self.cleaned_data.get('first_name', 'CustomUserForm instance')
        last_name = self.cleaned_data.get('last_name', 'CustomUserForm instance')
        email = self.cleaned_data.get('email', 'CustomUserForm instance')
        password1 = self.cleaned_data.get('password1', 'CustomUserForm instance')
        password2 = self.cleaned_data.get('password2', 'CustomUserForm instance')
        return f"CustomUserForm for user: {username} {first_name} {last_name} {email} {password1} {password2}"