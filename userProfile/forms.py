from django import forms
from .models import *

# Profile forms

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile        
        fields = '__all__'
        exclude = ['user','date_updated', 'verified', 'date_created', 'code', 'recommended_by']

        widgets = {            
            'first_name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'First name...'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last name...'}),
            'gender' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Gender..'}),            
            'phone' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phone..'}),            
            'date_of_birth' : DateInput(attrs={'class': 'form-control','placeholder': 'Date of birth..'}),
            'address' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Address..'}),
            'city' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'City..'}),            
            'country' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Country..'}),            
            'profile_pic' : forms.FileInput(attrs={'class': 'form-control','placeholder': 'Profile image ..'}),
            'id_copy' : forms.FileInput(attrs={'class': 'form-control','placeholder': 'ID/Passport..'}),
            'wallet_address' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Wallet address..'}),
            'wallet_currency' : forms.Select(attrs={'class': 'form-control col-md-12'}),
            }
        