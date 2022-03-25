from django.urls import path, include
from .views import *

#About us Urls
urlpatterns = [    
    path('', aboutUs_view, name='about-us'),    
]
