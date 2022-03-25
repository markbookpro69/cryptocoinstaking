from django.urls import path, include
from .views import *

# Crypto Rates Urls
urlpatterns = [    
    path('', cryptoRates_view, name='crypto-rates'),    
]
