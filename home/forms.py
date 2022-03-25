from django.forms import ModelForm
from django import forms
from .models import *

 
#applications Forms

class DateInput(forms.DateInput):
    input_type = 'date'

class SubscriberForm(forms.ModelForm):
       
     class Meta:
        model = Subscriber
        fields = '__all__'
                  
        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Subscribe to newsletter'}),            
            }       
    