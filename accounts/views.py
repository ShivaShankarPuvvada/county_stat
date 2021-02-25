from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import ProfileChangeFrom

from . import forms

class SignUp(CreateView):
    form_class = forms.ProfileCreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("myapp/register")


class ProfileUpdate(UpdateView):
    # form = ProfileChangeFrom(instance="username")
    form_class = forms.ProfileChangeFrom
    success_url = reverse_lazy("home")
    template_name = "accounts/profile.html"
