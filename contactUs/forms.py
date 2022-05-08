from django.forms import ModelForm
from django import forms
from .models import *

 
#applications Forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
       
     class Meta:
        model = Contact
        fields = '__all__'
                  
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'check-form','placeholder': 'Name'}),
            'email' : forms.EmailInput(attrs={'class': 'check-form','placeholder': 'E-mail'}),
            'message' : forms.Textarea(attrs={'class': 'check-form','placeholder': 'Message'}),            
            }       
    