from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from myapp.models import Agency
 
class AgencyResource(resources.ModelResource):
    class Meta:
        model = Agency
        fields = ('system_name', 'county', 'state', 'active', 
            'system_type', 'address', 'city', 'zipcode','system_no' )
        
        import_id_fields = ['system_name', 'system_no']


# class SystemNoResource(resources.ModelResource):
#     system_name = fields.Field(
#         column_name='system_name',
#         attribute='system_name',
#         widget=ForeignKeyWidget(Agency, 'system_name'))

#     class Meta:
#         model = SystemNumber
#         fields = ('system_name', 'system_no')
