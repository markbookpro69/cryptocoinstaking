from django.shortcuts import render
from .models import Affiliates
from django.contrib.auth.decorators import login_required

# Affiliates Views Here
@login_required
def affiliate_view(request):
    downliners = Affiliates.objects.filter(benefiter = request.user)

    context = {
        'downliners':downliners,
    }
    return render(request, 'affiliates/affiliates-list.html', context)
