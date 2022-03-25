from django.shortcuts import render
from .models import Affiliates

# Affiliates Views Here
def affiliate_view(request):
    downliners = Affiliates.objects.filter(benefiter = request.user)

    context = {
        'downliners':downliners,
    }
    return render(request, 'affiliates/affiliates-list.html', context)
