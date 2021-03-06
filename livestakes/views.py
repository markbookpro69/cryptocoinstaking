from django.shortcuts import render
from investments.models import Investment
from pycoingecko import CoinGeckoAPI

# Livestake Views Here
def liveStake_view(request):
    all = Investment.objects.all().order_by('-date_created')
    #Live Crypto rates from coingeckoapi
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'dogecoin', 'ripple', 'dash', 'usd-coin',
                     'polkadot', 'bitcoin-cash', 'binancecoin', 'tether', 'stellar', 'cosmos'], vs_currencies='usd')
    bch = p['bitcoin-cash']['usd']
    usdc = p['usd-coin']['usd']

    context = {
        'invmt': all,
        'price':p,
        'bch':bch,
        'usdc':usdc,
    }
    return render(request, 'livestakes/live-feed.html', context)
