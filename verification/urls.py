from django.urls import path, include
from .views import *

#Livestakes Urls
urlpatterns = [    
    path('', verification_view, name='verify'),    
]
