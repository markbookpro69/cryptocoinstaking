from django.shortcuts import render
from settings.models import Setting
from .models import Interest
from django.contrib.auth.decorators import login_required

# Interest views here.
@login_required
def interest_list_view(request):
    interests = Interest.objects.filter(user = request.user, amount_in_coin__gt=0)

    #summary section
    user = Setting.objects.get(user = request.user)
    coin_symbol = user.coin
    context = {
        'interests':interests,
        'coin_symbol':coin_symbol,
    }
    return render(request, 'interests/interest-list.html', context)
