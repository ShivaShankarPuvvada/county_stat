from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from myapp.models import (Agency)

# Register your models here.
@admin.register(Agency)
class AgencyAdmin(ImportExportModelAdmin):
    list_display = ('system_name', 'county', 'state', 'active', 'system_type', 'address', 'city', 'zipcode', 'system_no',)

# admin.site.register(Agency)
# @admin.register(SystemNumber)
# class SystemNoAdmin(ImportExportModelAdmin):
#     list_display = ('system_name', 'system_no')
#     pass
# admin.site.register(SystemNumber)
