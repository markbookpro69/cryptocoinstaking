from django.shortcuts import render, redirect
from .forms import ContactForm

# Contact us Views Here
def contactUs_view(request):
    form = ContactForm()
    if request.method == 'POST':        
        form = ContactForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('contact-us')

    context = {
        'form': form,
    }
    return render(request, 'contactUs/contact-us.html', context)
