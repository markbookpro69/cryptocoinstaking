from django.db import models
from django.contrib.auth.models import User

# Bank models here

class Current_Bank_Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 15, decimal_places = 4, null=False, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " | " + self.user.email + " | " + str(self.amount)

class Affiliate_Bank_Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 15, decimal_places = 4, null=False, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username) + " | " + str(self.amount)

class Interest_Bank_Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 15, decimal_places = 4, default=0, null=True, blank=True,)

    def __str__(self):
        return self.user.username + " | " + self.user.email + " | " + str(self.amount)

class Withdrawal_Bank_Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 15, decimal_places = 2, default=0, null=True, blank=True,)

    def __str__(self):
        return self.user.username + " | " + self.user.email + " | " + str(self.amount)

