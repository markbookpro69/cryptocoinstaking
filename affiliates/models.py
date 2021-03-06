from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Affiliates models here.

class Affiliates(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    affiliate_ref = models.CharField(max_length = 6, unique=True, blank=True, null=True)
    benefiter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='benefiter')
    amount = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    status = models.BooleanField(default=False)
    credit_status = models.CharField(max_length = 10, default='Processing', blank=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username) 
