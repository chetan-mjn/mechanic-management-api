from django.db import models

class Mechanic(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    is_open = models.BooleanField(default=True)
    services = models.JSONField()
 
