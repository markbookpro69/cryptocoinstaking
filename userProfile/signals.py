from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import User_profile
from verification.models import Verification
from settings.models import Setting
from bank.models import *
import uuid


#Profile signals

def user_profile(sender, instance, created, **kwargs):
    if created:       
        code = str(uuid.uuid4()).replace("-", "")[:12]
        User_profile.objects.create(
            user=instance,
            code=code            
            )
        Verification.objects.create(
            user = instance,
            code = code,
        )
        Setting.objects.create(
            user = instance,            
        ) 
        Current_Bank_Account.objects.create(
            user = instance,
            amount = 0,            
        )
        Affiliate_Bank_Account.objects.create(
            user = instance, 
            amount = 0,           
        )
        Interest_Bank_Account.objects.create(
            user = instance,
            amount = 0,            
        ) 
        Withdrawal_Bank_Account.objects.create(
            user = instance,
            amount = 0,            
        )           
post_save.connect(user_profile, sender=User)