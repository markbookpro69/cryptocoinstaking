from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bank.models import *

# Compound Interest views here.


@login_required
def compound_interest_view(request):
    user1 = Interest_Bank_Account.objects.get(user=request.user)
    user2 = Current_Bank_Account.objects.get(user=request.user)
    interest_amount = user1.amount
    current_amount = user2.amount

    Current_Bank_Account.objects.filter(user=request.user).update(
        amount=interest_amount + current_amount
    )
    Interest_Bank_Account.objects.filter(user=request.user).update(
        amount=0
    )
    return redirect('dashboard')

@login_required
def compound_affiliate_bonus_view(request):
    user1 = Affiliate_Bank_Account.objects.get(user=request.user)
    user2 = Current_Bank_Account.objects.get(user = request.user)
    affiliate_amount = user1.amount
    current_amount = user2.amount
    
    Current_Bank_Account.objects.filter(user = request.user).update(
        amount = affiliate_amount + current_amount
    )
    Affiliate_Bank_Account.objects.filter(user = request.user).update(
        amount = 0
    )
    return redirect('dashboard')