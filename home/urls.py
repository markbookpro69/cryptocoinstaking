from django.urls import path, include
from .views import *

#Home Urls
urlpatterns = [    
    path('', home_view, name='home'),    
]
