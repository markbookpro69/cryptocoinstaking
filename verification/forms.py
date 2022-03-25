from django import forms
from .models import *

# verification forms

class DateInput(forms.DateInput):
    input_type = 'date'

class verificationForm(forms.ModelForm):
    class Meta:
        model = Verification        
        fields = '__all__'
        exclude = ['user','status']

        widgets = {            
            'code' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Verification code...'}),
            }
        