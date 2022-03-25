from django.shortcuts import render

# About us Views Here
def aboutUs_view(request):
    return render(request, 'aboutUs/about-us.html')
