from django.shortcuts import render
# from watero.forms import UserForm, UserProfileInfoForm, AgencyInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required # this one requires login from user. 
from django.views.generic import (TemplateView, ListView, DetailView)


class AboutView(TemplateView):
    template_name = 'myapp/about.html'
class ThanksPage(TemplateView):
    template_name = 'myapp/thanks.html'
class RegisterPage(TemplateView):
    template_name = 'myapp/register.html'

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')