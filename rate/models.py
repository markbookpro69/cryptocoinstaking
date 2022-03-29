from django.db import models

# Rates models here.

class Rate(models.Model):
    interest_rate = models.DecimalField(max_digits = 15, decimal_places = 4,)
    affiliate_rate = models.IntegerField(null=True, blank=True)
    minimum_withdrawal = models.DecimalField(max_digits = 15, decimal_places = 2,)
    minimum_investment = models.DecimalField(max_digits = 15, decimal_places = 2,)
    withdrawal_fee = models.DecimalField(max_digits = 15, decimal_places = 1,)
    fake = models.DecimalField(max_digits = 15, decimal_places = 1,)

    def __str__(self):
        return str(self.interest_rate) + " " + str(self.affiliate_rate)