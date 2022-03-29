from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_amount = models.DecimalField(max_digits = 15, decimal_places = 4, null=True, blank=True,)
    interest_rate = models.DecimalField(max_digits = 15, decimal_places = 4, null=True, blank=True,)
    amount_in_coin = models.DecimalField(max_digits = 15, decimal_places = 4, null=True, blank=True,)
    amount_in_usd = models.DecimalField(max_digits = 15, decimal_places = 4, null=True, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username +" | "+ str(self.investment_amount) 