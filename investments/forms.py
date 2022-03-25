from django.forms import ModelForm
from django import forms
from .models import *

 
#applications Forms

class DateInput(forms.DateInput):
    input_type = 'date'

class investmentAmountForm(forms.ModelForm):
       
     class Meta:
        model = Investment
        fields = '__all__'
        exclude = ['user', 'invstmt_ref', 'amount_in_usd', 'status']
          
        widgets = {
            'amount' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Amount'}),            
            }       
    