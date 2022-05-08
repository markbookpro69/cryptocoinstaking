from decimal import Decimal
from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
from django.contrib.auth.decorators import login_required
from accounts.decorators import unverified_user
from affiliates.models import Affiliates
from settings.models import *
from bank.models import *
from investments.models import Investment
from bank.models import Current_Bank_Account
from django.db.models import Sum
from rate.models import Rate
from userProfile.models import User_profile


# Dashboard Views Here


@unverified_user
def dashboard_view(request):
    #update current
    complete_investment = Investment.objects.filter(user = request.user, status = 'completed').aggregate(Sum('amount'))['amount__sum']
    affiliate_bonus = Affiliates.objects.filter(benefiter = request.user, status = False).aggregate(Sum('amount'))['amount__sum']
    available_current_amount = Current_Bank_Account.objects.get(user = request.user)
    available_affiliate_amount = Affiliate_Bank_Account.objects.get(user = request.user)
    current_affiliate_amount = available_affiliate_amount.amount
    current_amount = available_current_amount.amount

    allowed_rate = Rate.objects.get(id = 1)
    affiliate_allowed_bonus = allowed_rate.affiliate_allowed_bonus

    if complete_investment is not None:
        Current_Bank_Account.objects.filter(user = request.user).update(
            amount = current_amount + complete_investment
        )
        Investment.objects.filter(user = request.user, status = 'completed').update(
            status = 'Credited'
        )         
    else:
        pass


    #update affiliate
    if affiliate_bonus is not None:
        Affiliate_Bank_Account.objects.filter(user = request.user).update(
            amount = affiliate_bonus + current_affiliate_amount
        )
        Affiliates.objects.filter(benefiter = request.user).update(
            status = True
        )

    #Live Crypto rates from coingeckoapi
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    bch = p['bitcoin-cash']['usd']
    usdc = p['usd-coin']['usd']

    #summary section
    user = Setting.objects.get(user = request.user)
    coin_symbol = user.coin
    coin_id = user.coin.coin_id
    coin_price = Decimal(p[coin_id]['usd'])

        
    user = Current_Bank_Account.objects.get(user = request.user)
    total_amount_in_current_account = user.amount
    total_amount_in_current_account_usd = "{:.4f}".format(total_amount_in_current_account * coin_price)

    #generated Interest
    user = Interest_Bank_Account.objects.get(user = request.user)
    total_amount_in_interest_account = user.amount
    total_amount_in_interest_account_usd = "{:.4f}".format(total_amount_in_interest_account * coin_price)

    #affiliate bonus
    user = Affiliate_Bank_Account.objects.get(user = request.user)
    total_amount_in_affiliate_account = user.amount
    total_amount_in_affiliate_account_usd = "{:.4f}".format(total_amount_in_affiliate_account * coin_price)

    #withdrawal amount
    user = Withdrawal_Bank_Account.objects.get(user = request.user)
    total_amount_withdrawn = user.amount
    total_amount_withdrawn_in_usd = "{:.4f}".format(total_amount_withdrawn * coin_price)

    #compund sections
    user1 = Affiliate_Bank_Account.objects.get(user=request.user)
    user2 = Interest_Bank_Account.objects.get(user = request.user)
    affiliate_amount = user1.amount
    interest_amount = user2.amount

    downliners = User_profile.objects.filter(recommended_by = request.user)
    context = {
        'bch':bch,
        'usdc':usdc,
        'price': p,

        #summery section
        'coin': coin_symbol,
        'current_amount': total_amount_in_current_account,
        'curent_amount_in_usd':total_amount_in_current_account_usd,

        #generated Interest
        'interest_amount': total_amount_in_interest_account,
        'interest_amount_in_usd':total_amount_in_interest_account_usd,

        #affiliate section
        'affiliate_amount': total_amount_in_affiliate_account,
        'affiliate_amount_in_usd':total_amount_in_affiliate_account_usd,

        #withdrawal section
        'withdrawal_amount': total_amount_withdrawn,
        'withdrawal_amount_in_usd':total_amount_withdrawn_in_usd,

        #compund section
        'compound_affiliate_amount':affiliate_amount,
        'compound_interest_amount':interest_amount,

        #Downliners
        'downliners':downliners,

        'affiliate_allowed_bonus':affiliate_allowed_bonus,
        
    }
    return render(request, 'dashboard/dashboard.html', context)
