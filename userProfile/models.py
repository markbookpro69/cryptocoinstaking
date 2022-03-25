from django.db import models
from django.contrib.auth.models import User
from settings.models import Coin


# Profile models here.
class User_profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    #common fields
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)    
    date_of_birth =models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)      
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='avatas/', blank=True, null=True) 
    id_copy = models.ImageField(upload_to='verifications/', blank=True, null=True)   
    verified = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #Banking Details
    wallet_address = models.CharField(max_length=200, blank=True, null=True)
    wallet_currency = models.ForeignKey(Coin, verbose_name=("Coin"), null=True, blank=True, on_delete=models.CASCADE)

    #Banking Details
    code = models.CharField(max_length=12, unique=True)
    recommended_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='ref_by')

    def __str__(self):
        return str(self.user.username)+ ' | ' + str(self.user.email)

    def get_recommended_profiles(self):
        pass

    
