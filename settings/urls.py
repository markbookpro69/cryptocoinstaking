from django.urls import path, include
from .views import *

#Settings Urls
urlpatterns = [    
    path('', settings_view, name='settings'),    
]
