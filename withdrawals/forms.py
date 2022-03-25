from django.forms import ModelForm
from django import forms
from .models import *

 
#applications Forms

class DateInput(forms.DateInput):
    input_type = 'date'

class withdrawInvestmentForm(forms.ModelForm):
       
     class Meta:
        model = Withdrawal
        fields = '__all__'
        exclude = ['user', 'amount_in_usd', 'withdrawal_type', 'status']
          
        widgets = {
            'amount' : forms.NumberInput(attrs={'class': 'form-control form-control','placeholder': 'Amount'}),            
            } 

class withdrawInterestForm(forms.ModelForm):
       
     class Meta:
        model = Withdrawal
        fields = '__all__'
        exclude = ['user', 'amount_in_usd', 'withdrawal_type', 'status']
          
        widgets = {
            'amount' : forms.NumberInput(attrs={'class': 'form-control form-control','placeholder': 'Amount'}),            
            }      
    