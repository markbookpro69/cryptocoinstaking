from django.db import models
from django.contrib.auth.models import User

# withdrawal models here.

class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 15, decimal_places = 4, default=0, null=True, blank=True,)
    amount_in_usd = models.DecimalField(max_digits = 15, decimal_places = 4, default=0, null=True, blank=True,)
    withdrawal_type = models.CharField(max_length=15)
    status = models.CharField(max_length=15, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " | " + str(self.amount) + " | " + str(self.withdrawal_type)
