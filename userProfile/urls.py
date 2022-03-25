from django.urls import path, include
from .views import *

#Profile Urls
urlpatterns = [    
    path('<int:pk>', profile_view, name='profile'),      
]
