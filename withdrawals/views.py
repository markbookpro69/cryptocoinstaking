from decimal import Decimal
from django.shortcuts import render, redirect
from settings.models import Setting
from userProfile.models import User_profile
from pycoingecko import CoinGeckoAPI
from bank.models import *
from rate.models import Rate
from .models import Withdrawal
from alfacoins_api_python import ALFACoins
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


# investments views here.
alfacoins = ALFACoins(
    name='Crypto Coin Staking',
    password='BTj9G3!kfubMEud',
    secret_key='b502070e80698ba490ec6350e291e16f'
    )

# Withdrawals Views Here
@login_required
def withdrawals_view(request):  

    #summary section
    withdrawals = Withdrawal.objects.filter(user = request.user)
    user_settings = Setting.objects.get(user = request.user)
    coin_symbol = user_settings.coin
    coin_id = user_settings.coin.coin_id 

    context = {
        'withdrawals':withdrawals,
        'coin_symbol':coin_symbol,
        'coin_id':coin_id,
               
    }
    return render(request, 'withdrawals/withdrawals.html', context)

@login_required
def withdrawal_investment_view(request):
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    #summary section
    user_settings = Setting.objects.get(user = request.user)
    coin_symbol = user_settings.coin
    coin_id = user_settings.coin.coin_id    
    coin_price = Decimal(p[coin_id]['usd'])

    min_withdrawal = Rate.objects.get(id = 1)
    minimum = "{:.2f}".format(min_withdrawal.minimum_withdrawal)
    fee =  min_withdrawal.withdrawal_fee
    
  
    user_wallet = User_profile.objects.get(user = request.user)
    wallet = user_wallet.wallet_address
   
    user_current_account = Current_Bank_Account.objects.get(user = request.user)
    total_amount_in_current_account = user_current_account.amount
    total_amount_in_current_account_usd = "{:.4f}".format(total_amount_in_current_account * coin_price)
    
    form = withdrawInvestmentForm()

    if request.method == 'POST':
        form = withdrawInvestmentForm(request.POST or None, request.FILES or None) 
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            request.session['amount'] = str(amount)
            request.session['type'] = 'Investment'
            return redirect('withdraw')
    context = {
        'min_withdrawal':minimum,
        'coin_symbol':coin_symbol,
        'coin_id':coin_id,
        'form':form,
        'fee':fee,

        'wallet':wallet,
        'current_amount': total_amount_in_current_account,
        'curent_amount_in_usd':total_amount_in_current_account_usd,
    }
    return render(request, 'withdrawals/withdrawal-investment.html', context)


@login_required
def withdrawal_interest_view(request):
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    #summary section
    user_settings = Setting.objects.get(user = request.user)
    coin_symbol = user_settings.coin
    coin_id = user_settings.coin.coin_id
    coin_price = Decimal(p[coin_id]['usd'])

    min_withdrawal = Rate.objects.get(id = 1)
    minimum = "{:.4f}".format(min_withdrawal.minimum_withdrawal)
    fee =  min_withdrawal.withdrawal_fee
    

    user_wallet = User_profile.objects.get(user = request.user)
    wallet = user_wallet.wallet_address

     #generated Interest
    user_interest_account = Interest_Bank_Account.objects.get(user = request.user)
    total_amount_in_interest_account = user_interest_account.amount
    total_amount_in_interest_account_usd = "{:.4f}".format(total_amount_in_interest_account * coin_price)

    form = withdrawInterestForm()

    if request.method == 'POST':
        form = withdrawInterestForm(request.POST or None, request.FILES or None) 
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            request.session['amount'] = str(amount)
            request.session['type'] = 'Interest'
            return redirect('withdraw')

    context = {
        'min_withdrawal':minimum,
        'coin_symbol':coin_symbol,
        'coin_id':coin_id,
        'form':form,
        'fee':fee,

        'wallet':wallet,
         #generated Interest
        'interest_amount': total_amount_in_interest_account,
        'interest_amount_in_usd':total_amount_in_interest_account_usd,
    }
    return render(request, 'withdrawals/withdrawal-interest.html', context)

@login_required
def withdraw(request):
    user_settings = Setting.objects.get(user = request.user)
    alfa_coin_id = user_settings.coin.alfacoins_id

    user_wallet = User_profile.objects.get(user = request.user)
    wallet = user_wallet.wallet_address

    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    #summary section
    user_settings = Setting.objects.get(user = request.user)    
    coin_id = user_settings.coin.coin_id
    coin_price = Decimal(p[coin_id]['usd'])

    min_withdrawal = Rate.objects.get(id = 1)    
    fee = min_withdrawal.withdrawal_fee
    amounts = request.session.get('amount')
    deduct = fee / 100 * amounts
    amount = amounts - deduct
    

    type = request.session.get('type')

    total_amount = "{:.4f}".format(Decimal(amount) * coin_price)

    email = request.user.email
    username = request.user.username

    
    try:
        result = alfacoins.bitsend(
                type = alfa_coin_id,
                coin_amount = amount,
                recipient_name =  username,  
                recipient_email = email,
                reference = 'Ref: Cryto Coin Staking Withdrawal',          
                options={                  
                    'address': wallet,
                    'memo': 'Memo: Cryto Coin Staking Withdrawal',                
                    #'amount': 1.23412341,                      
                    },   
            ) 
        
        if type == 'Investment':
            user_amount = Current_Bank_Account.objects.get(user = request.user)
            available_amount = user_amount.amount
            Current_Bank_Account.objects.filter(user = request.user).update(
                amount = available_amount - Decimal(amounts)
            )
        elif type == 'Interest':
            user_amount = Interest_Bank_Account.objects.get(user = request.user)
            available_amount = user_amount.amount
            Interest_Bank_Account.objects.filter(user = request.user).update(
                amount = available_amount - Decimal(amounts)
            )
        else:
            pass

        Withdrawal.objects.create(
            user = request.user,
            amount = amounts,
            amount_in_usd = total_amount,
            withdrawal_type = type,
            status = 'Withdrawn'
        )
    except:
        messages.success(request, 'Error Contact Support')
        return redirect('withdrawals')

    context = {
        'result':result,
    }
    return render(request, 'withdrawals/withdraw.html', context)