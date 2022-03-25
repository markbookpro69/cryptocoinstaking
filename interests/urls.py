from django.urls import path, include
from .views import *

#interest Urls
urlpatterns = [    
    path('', interest_list_view, name='interest-list'),       
]
