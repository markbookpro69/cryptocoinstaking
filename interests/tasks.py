from django.contrib.auth import get_user_model
from celery import shared_task
from rate.models import Rate
from decimal import Decimal
from bank.models import Interest_Bank_Account, Current_Bank_Account
from pycoingecko import CoinGeckoAPI
from settings.models import Setting
from .models import Interest


@shared_task(bind=True)
def update_interest(self):    
    User = get_user_model()
    users = User.objects.all()

    #Interest
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')

    for user in users:

        #Interest               
        obtain_total = Current_Bank_Account.objects.get(user = user)        
        total_investment = obtain_total.amount

        user_setting = Setting.objects.get(user = user)        
        coin_id = user_setting.coin.coin_id
        coin_price = Decimal(p[coin_id]['usd'])
       
        fixed_rate = Rate.objects.get()
        rate = fixed_rate.interest_rate
        total_interest = Decimal(rate / 100) * total_investment                
        total_interest_usd = "{:.4f}".format(total_interest * coin_price)

        
        Interest.objects.create(
            user = user,
            investment_amount = total_investment,            
            interest_rate = rate,
            amount_in_coin = total_interest, 
            amount_in_usd = total_interest_usd,
        )

        get_amount = Interest_Bank_Account.objects.get(user = user)
        coins = get_amount.amount
        print(coins)
        Interest_Bank_Account.objects.filter(user = user).update(            
            amount = coins + total_interest
        )
    return "Done: " 
