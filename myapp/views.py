from django.shortcuts import render
from .resources import AgencyResource, SystemNoResource
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
    error_import = None
    success_import = None
    if request.method == 'POST':
        agency_resource = AgencyResource()
        system_resource = SystemNoResource()
        dataset = Dataset()
        new_r = request.FILES['myfile']

        imported_data = dataset.load(new_r.read().decode('utf-8'),format='csv')
        result = agency_resource.import_data(dataset, dry_run=True)  # Test the data import
        result = system_resource.import_data(dataset, dry_run=True)
        
        # if result.is_valid():
        #     success_import = "import Successful..."
        if not result.has_errors():
            error_import = "Oops. something went wrong could not import..."
            agency_resource.import_data(dataset, dry_run=False)  # Actually import now
            system_resource.import_data(dataset, dry_run=False) 
    return render(request, 'myapp/importer.html')

