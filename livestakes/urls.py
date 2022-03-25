from django.urls import path, include
from .views import *

#Livestakes Urls
urlpatterns = [    
    path('', liveStake_view, name='live-stakes'),    
]
