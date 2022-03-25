from django.contrib import admin
from .models import *

# bank admin models here.
admin.site.register(Current_Bank_Account)
admin.site.register(Affiliate_Bank_Account)
admin.site.register(Interest_Bank_Account)
admin.site.register(Withdrawal_Bank_Account)
