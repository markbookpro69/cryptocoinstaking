from django.shortcuts import render, redirect
from home.forms import SubscriberForm

# About us Views Here
def aboutUs_view(request):
    form = SubscriberForm()
    if request.method == 'POST':        
        form = SubscriberForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form':form,
    }
    return render(request, 'aboutUs/about-us.html', context)
