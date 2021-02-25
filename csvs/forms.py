from django import forms
from .models import Csv

CSV_Choices= [
    (0, 'Please select the file content'),
    (1, 'Angencies and System Numbers'),
    (2, 'Other'),

    ]

class CsvForm(forms.ModelForm):
    # CSV_intf= forms.CharField(label='What is this file?', widget=forms.Select(choices=CSV_Choices))
    class Meta:
        model = Csv
        
        fields = ('file_name',)
        
