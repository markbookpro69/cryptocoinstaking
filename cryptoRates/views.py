from django.shortcuts import render
from pycoingecko import CoinGeckoAPI

# Crypto Rates Views Here
def cryptoRates_view(request):
   
    #Live Crypto rates from coingeckoapi
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    bch = p['bitcoin-cash']['usd']
    usdc = p['usd-coin']['usd']

    context = {
        'price':p,
        'bch':bch,
        'usdc':usdc,
    }
    return render(request, 'cryptoRates/crypto-rates.html', context)
