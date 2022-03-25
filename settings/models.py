from django.db import models
from django.contrib.auth.models import User

# Settings models here.

class Coin(models.Model):
    coin_name = models.CharField(max_length=6)
    coin_id = models.CharField(max_length=12)
    alfacoins_id = models.CharField(max_length=50)
    is_staking = models.BooleanField(default=True)    
    
    def __str__(self):
        return str(self.coin_name)

class Setting(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)    
    coin = models.ForeignKey(Coin, verbose_name=("Coin"), default=1, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + " | " + str(self.coin)