from django.db import models
from django.contrib.auth.models import User

# Investment models here.

class Investment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invstmt_ref = models.CharField(max_length = 6, unique=True, blank=True, null=False)
    amount = models.DecimalField(max_digits = 15, decimal_places = 2, null=False,)
    amount_in_usd = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    status = models.CharField(max_length = 10, default='Processing', blank=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email + " | " + str(self.amount)