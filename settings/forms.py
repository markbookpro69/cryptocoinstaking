from django import forms
from .models import *

# Settings forms

class DateInput(forms.DateInput):
    input_type = 'date'
    
class settingsForm(forms.ModelForm):

    
    class Meta:
        model = Setting        
        fields = '__all__'
        exclude = ['user']

        widgets = {            
            'coin': forms.Select(attrs={'class': 'form-control col-md-12'}),
            }
        