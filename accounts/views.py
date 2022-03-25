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
            request.session['ref_profile'] = profile.id
            profile_id = request.session.get('ref_profile')
            print('id', profile.id)

            if form.is_valid():
                if profile_id is not None:
                    recommended_by_profile = User_profile.objects.get(
                        id=profile_id)
                    
                    registered_user = User.objects.get(id=user.id)
                    registered_profile = User_profile.objects.get(
                        user=registered_user)
                    registered_profile.recommended_by = recommended_by_profile.user
                    groupname = 'Users'
                    group = Group.objects.get(name=groupname)
                    user.groups.add(group)
                    name = form.cleaned_data.get('username')
                    user = form.save()
                    registered_profile.save()
                    messages.success(
                        request, 'Account created successfully for ' + name)                    
                    return redirect('login')

                else:                    
                    groupname = 'Users'
                    group = Group.objects.get(name=groupname)
                    user.groups.add(group)
                    name = form.cleaned_data.get('username')
                    user = form.save()
                    messages.success(
                        request, 'Account created successfully for ' + name)                    
                    return redirect('login')
        except:
            form.save()
            messages.success(request, 'Account created successfully')            
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'accounts/create-account.html', context)
