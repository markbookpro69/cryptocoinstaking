from django.shortcuts import redirect, render
from pycoingecko import CoinGeckoAPI
from rate.models import Rate
from .forms import SubscriberForm
 
# Home Views Here
def home_view(request):
    min_withdrawal = Rate.objects.get(id = 1)
    rate = min_withdrawal.interest_rate
    daily = min_withdrawal.fake

    #Live Crypto rates from coingeckoapi
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    bch = p['bitcoin-cash']['usd']
    usdc = p['usd-coin']['usd']

    form = SubscriberForm()
    if request.method == 'POST':        
        form = SubscriberForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'rate':rate,
        'daily':daily,
        'price':p,
        'bch':bch,
        'usdc':usdc,
        'form':form,

    }
    
    return render(request, 'home/home.html', context)
