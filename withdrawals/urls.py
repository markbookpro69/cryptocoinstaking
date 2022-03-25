from django.urls import path, include
from .views import *

#Livestakes Urls
urlpatterns = [    
    path('', withdrawals_view, name='withdrawals'),   
    path('withdraw-investment/', withdrawal_investment_view, name='withdrawal-investment'), 
    path('withdraw-interest/', withdrawal_interest_view, name='withdrawal-interest'),
    path('withdraw/', withdraw, name='withdraw'), 

]
