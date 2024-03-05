"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpRequest
from .forms import RegisterUserForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def register_user(request):
    """Renders the register page."""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(
        request,
        'app/register.html',
        {
            'title': 'Create your user account.',
            'message': 'Your user sign up page.',
            'form': form,
            'year': datetime.now().year,
        }
    )


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "app/register.html"