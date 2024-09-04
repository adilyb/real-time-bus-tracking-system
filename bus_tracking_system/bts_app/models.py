from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Location({self.latitude}, {self.longitude})"
    