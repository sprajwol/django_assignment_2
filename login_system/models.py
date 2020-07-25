from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='uploads/profiles/', blank=True, null=True)
    current_address = models.CharField(max_length=100, blank=True)
    primary_phone_number = models.CharField(max_length=15, blank=True)
    secondary_phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.user.username}'s Profile")
