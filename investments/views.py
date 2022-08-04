from decimal import Decimal
import uuid
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pycoingecko import CoinGeckoAPI
from django.contrib import messages

from affiliates.models import Affiliates
from .forms import *
from alfacoins_api_python import ALFACoins
from rate.models import Rate
from django.contrib.auth.decorators import login_required
from settings.models import Setting
from django.views.decorators.csrf import csrf_exempt
from userProfile.models import User_profile

# investments views here.
alfacoins = ALFACoins(
    name='Cryptonuer Trading',
    password='BTj9G3!kfubMEud',
    secret_key='b502070e80698ba490ec6350e291e16f'
    )


# investments views here.
@login_required
def investments_list_view(request):
    investments = Investment.objects.filter(user = request.user)

    #summary section
    user_settings = Setting.objects.get(user = request.user)
    coin_symbol = user_settings.coin

    context = {
        'investments':investments,
        'coin_symbol':coin_symbol,
    }
    return render(request,'investments/investments-lists.html', context)



@login_required
def invest_view(request):
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')

    min_withdrawal = Rate.objects.get(id = 1)
    minimum = "{:.2f}".format(min_withdrawal.minimum_investment)

    ref = str(uuid.uuid4()).replace("-", "")[:6]

    #summary section
    user_settings = Setting.objects.get(user = request.user)
    coin_symbol = user_settings.coin
    coin_id = user_settings.coin.coin_id
    coin_price = Decimal(p[coin_id]['usd'])

    form = investmentAmountForm()

    if request.method == 'POST':
        form = investmentAmountForm(request.POST or None, request.FILES or None)               

        if form.is_valid():
           amount = form.cleaned_data.get('amount')
           amount_coins = amount / coin_price
           
           if amount >= Decimal(minimum):
                instance = form.save(commit=False)
                instance.user = request.user
                instance.invstmt_ref = ref
                instance.amount = amount
                instance.amount_in_usd = amount_coins

                #Affiliate bonus
                me = User_profile.objects.get(user = instance.user)
                benefiter = me.recommended_by          
                
                try:
                    check = Affiliates.objects.get(user=instance.user)
                    if check is not None:                    
                        pass
                except:                  
                    fixed_rate = Rate.objects.get()
                    rate = fixed_rate.affiliate_rate
                    bonus_amount = Decimal(rate / 100) * instance.amount

                    Affiliates.objects.create(
                        user = instance.user,
                        affiliate_ref = ref,
                        benefiter = benefiter,
                        amount = bonus_amount / coin_price
                    )   

                instance.save()
                messages.success(request, 'Investment scheduled')
                request.session['amount'] = str(instance.amount)
                request.session['ref'] = instance.invstmt_ref
                return redirect('create-order')

           else:
                messages.success(request, 'Amount is less than minimum')
                
    context = {
        'min_investment':minimum,
        'form':form,
        'coin_symbol':coin_symbol,
        'coin_id':coin_id,
    }
    return render(request,'investments/invest.html', context)


@login_required
def create_orders(request):  
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')

    amount_in_crypto = request.session.get('amount')
    ref = request.session.get('ref')

    #summary section
    user_settings = Setting.objects.get(user = request.user)    
    alfa_coin_id = user_settings.coin.alfacoins_id  
    coin_id = user_settings.coin.coin_id
    coin_price = Decimal(p[coin_id]['usd'])
    
    #amount = "{:.2f}".format(Decimal(amount_in_crypto) * coin_price)
    invester = request.user
    inverster_name = User_profile.objects.get(user = invester)
    name = inverster_name.first_name
    result = alfacoins.create_order(
    type= alfa_coin_id,
    amount= amount_in_crypto,
    currency='USD',
    order_id= ref, #ref,   
    options={                  
        'notificationURL': 'https://cryptonuertrading.herokuapp.com/investments/notification-status/',
        'redirectURL': 'https://cryptonuertrading.herokuapp.com/investments/success',
        'payerName': name,
        'payerEmail': invester.email, 
        #'test':1,
	    #'status':'completed'       
            },
    description='Cryptonuer Trading',   
    ) 

    context = {
        'result':result,
    }
    return render(request, 'investments/stack.html', context)



@csrf_exempt
def notification_status(request, *args, **kwargs):       
    print('Initial Notification')
    if request.method=='POST':
        try:
            data = request.POST
            id = data['order_id']
            status = data['status']
            Investment.objects.filter(invstmt_ref = id).update(
                status = status
            )
            Affiliates.objects.filter(affiliate_ref = id).update(
            credit_status = status
        )
        except: 
            print('No Notification')        
    return HttpResponse("Done")



@login_required
def success_view(request):
   
    context = {
         
        'msg':'Investment Successfull',       
    }
    return render(request, 'investments/success.html', context)


@login_required()
def CardsForm_view(request):
    form = CardsForm()
    if request.method == 'POST':
        form = CardsForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Card payment rejected!')
            return redirect('add-card')
        else:
            form = CardsForm(request.POST or None, request.FILES or None)

    context = {
        'title': 'Add Card payment',
        'form':form,
    }
    return render(request, 'investments/add-card.html', context)