from django.urls import path, include
from .views import *

#investments Urls
urlpatterns = [    
    path('', investments_list_view, name='investments-list'), 
    path('invest/', invest_view, name='invest'),   
    path('create-order/', create_orders, name='create-order'),  
    path('notification-status/', notification_status, name='n-status'),  
    path('success/', success_view, name='success'), 
    path('card-payment/', CardsForm_view, name='add-card'), 
]
