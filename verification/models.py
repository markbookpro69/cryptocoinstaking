from django.db import models
from django.contrib.auth.models import User

# verification models here.

class Verification(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=12)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " " + str(self.code) + " " + " Verified:" + str(self.status)
