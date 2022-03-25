from django.urls import path, include
from .views import *

#Compound Urls
urlpatterns = [    
    path('', compound_interest_view, name='compound-interest'), 
    path('compound-bonus', compound_affiliate_bonus_view, name='compound-bonus'),   
]
