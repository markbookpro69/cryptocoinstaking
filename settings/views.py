from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Settings views here.


def settings_view(request):
    form = settingsForm()
    setting = Setting.objects.get(user = request.user)
    pressed = setting.is_selected
    if request.method == 'POST':        
        form = settingsForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            instance = form.save(commit=False)
            Setting.objects.filter(user = request.user).update(
                coin = instance.coin,
                is_selected = True,
            )
            messages.success(request, 'Settings updated successfully!')
            return redirect('profile', request.user.id)
        else:
            form = settingsForm()
            print(form.errors)

    context = {
        'pressed': pressed,
        'form':form,
    }
    return render(request, 'settings/settings.html', context)
