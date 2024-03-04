"""
Definition of forms.
"""

from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'placeholder': 'User name'
            }))

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            {
                'class': 'form-control',
                'placeholder': 'Password'
            }))


class RegisterUserForm(UserCreationForm):
    """Registration form which uses boostrap CSS."""
    email = forms.EmailField(
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'placeholder': 'your_email@provider.domain'
            }))

    first_name = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'placeholder': 'First name'
            }))

    last_name = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'placeholder': 'Last name'
            }))

    user_name = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            {
                'class': 'form-control',
                'placeholder': 'User name'
            }))

    class Meta:
        model = User
        fields = (
            'user_name',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )