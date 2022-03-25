from django.shortcuts import render
from .forms import *

# Profile Views Here

from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User_profile
#from .forms import CreateProfileForm


@login_required(login_url='login')
def profile_view(request, pk):
    profile = request.user.user_profile
    form = CreateProfileForm(instance=profile)    
    downliners = User_profile.objects.filter(recommended_by=request.user).count()
    
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')

    context = {
        'form': form, 
        'downliners':downliners, 
        'userinfo': profile,
        }
    return render(request, 'userProfile/profile.html', context)


