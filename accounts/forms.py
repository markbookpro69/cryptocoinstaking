from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

#Accounts forms


#Password Reset Form
class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user','placeholder': 'E-mail...', 'type': 'email',
        }))

#User Registration Form
class RegisterUserForm(UserCreationForm):

     password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Password...','type':'password'}),
        )

     password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Confirm Password','type':'password'}),
        )

     #group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True,empty_label='Choose account type', 
                                    #widget=forms.Select(attrs={'class': 'form-control form-control-user',})
                                   # )

     class Meta:
        model = User
        exclude = ['group']
        fields = [            
            'email',
            'username',            
            'password1',
            'password2',
           ]

        widgets = {           
            'email' : forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'E-mail...'}),
            'username' : forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Username..eg. johndoe'}),
           }