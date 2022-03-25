from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
