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
    

class CardsForm(forms.ModelForm):
       
     class Meta:
        model = Cards
        fields = '__all__'
          
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name on Card'}),  
            'number' : forms.NumberInput(attrs={'class': 'form-control','placeholder': '0000 0000 0000 0000'}),
            'expiry_date' : forms.TextInput(attrs={'class': 'form-control','placeholder': '01/23'}),      
            'cvv' : forms.NumberInput(attrs={'class': 'form-control','placeholder': '123'}),  
            'amount' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Amount'}),  
            }