from django.shortcuts import render, redirect
from pycoingecko import CoinGeckoAPI
from home.forms import SubscriberForm

# Crypto Rates Views Here
def cryptoRates_view(request):
   
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
        'price':p,
        'bch':bch,
        'usdc':usdc,
        'form':form,
    }
    return render(request, 'cryptoRates/crypto-rates.html', context)
