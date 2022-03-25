from django.urls import path, include
from .views import *

#Home Urls
urlpatterns = [    
    path('', affiliate_view, name='affiliate-bonuses'),    
]
