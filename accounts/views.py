from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from userProfile.models import User_profile
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from verification.models import Verification

# Accounts views here


@unauthenticated_user
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:                       
            print(user)
            login(request, user)
            return redirect('verify')

        else:
            messages.error(request, 'Incorrect credentials, retry!!')
            return render(request, 'accounts/login.html')

    context = {
        'login': 'login'
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def authentication_view(request):

    username = request.user.username
    email_address = request.user.email
    user = Verification.objects.get(user=request.user)
    code = user.code

    context = {
        'code': code,
        'email': email_address,
        'username': username,
    }
    template = render_to_string('accounts/verification_email.html', context)
    email = EmailMessage(
        'Verify your Account',
        template,
        settings.EMAIL_HOST_USER,
        [email_address],
    )
    email.fail_silently = False
    email.content_subtype = "html"
    email.send()
    messages.error(request, 'Email Sent, Please check your spam folder')
    return redirect('verify')


@unauthenticated_user
def register_view(request, *args, **kwargs):

    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST or None)
        
        try:
            code = str(kwargs.get('ref_code'))
            profile = User_profile.objects.get(code=code)
            recommender = profile.user
            print('rocommender', recommender)

            if form.is_valid():
                if recommender is not None:
                    instance = form.save(commit=False)
                    name = form.cleaned_data.get('username')
                    instance.save()
                                                                
                    User_profile.objects.filter(user = instance.id).update(
                        recommended_by = recommender 
                    )
                    messages.success(
                        request, 'Account created successfully for ' + name)                    
                    return redirect('login')                  

            
        except: 

            if form.is_valid():
                name = form.cleaned_data.get('username')
                form.save()
                messages.success(
                    request, 'Account created successfully for ' + name)                    
                return redirect('login') 
            else:
                messages.success(
                    request, 'Registration Failed')                    
                return redirect('create-account') 

    context = {
        'form': form,
    }
    return render(request, 'accounts/create-account.html', context)
