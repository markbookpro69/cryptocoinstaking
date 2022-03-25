from datetime import datetime
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm
from .views import *

#Accounts  urls

urlpatterns = [ 

     path('', login_view, name = 'login'),
     path('logout/', logout_view, name = 'logout'),   
     path('send-verification-code/', authentication_view, name = 'send-code'), 
     path('create-account', register_view, name='create-account'),
     path('<str:ref_code>', register_view, name='create-account'),
     

     #Django class views for password reset functionality
     path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/forgot-password.html",
         form_class = UserPasswordResetForm),
         name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
     
    ]

