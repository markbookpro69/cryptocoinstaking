from django.urls import path, include
from .views import *

#Dashboard Urls
urlpatterns = [    
    path('', dashboard_view, name='dashboard'),    
]
