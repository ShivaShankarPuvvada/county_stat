from django.shortcuts import render
from .resources import AgencyResource
from tablib import Dataset

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


# def export(request):
#     agency_resource = AgencyResource()
#     dataset = agency_resource.export()
#     response = HttpResponse(dataset.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="agency.csv"'
#     return response

def simple_upload(request):
    if request.method == 'POST':
        agency_resource = AgencyResource()
        dataset = Dataset()
        new_r = request.FILES['myfile']
        imported_data = Dataset().load(new_r.read().decode("utf-8"), format='csv')
        result = agency_resource.import_data(dataset, dry_run=True)  # Test the data import, give raise_errors = True as last parameter if you want to see errors.
        if not result.has_errors():
            agency_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'myapp/importer.html')

