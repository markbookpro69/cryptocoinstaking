from django.urls import path, include
from .views import *

#Contact us Urls
urlpatterns = [    
    path('', contactUs_view, name='contact-us'),    
]
