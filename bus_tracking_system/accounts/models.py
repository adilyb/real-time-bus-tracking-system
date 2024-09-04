from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    USER_ROLES = (
        ('driver', 'Driver'),
        ('office', 'Office Staff'),
        ('admin', 'Administrator'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return self.user.username

