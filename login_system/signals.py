from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import os

from login_system.models import Profile

# For auto matically creating a profile when a user is added in the user table created


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if (created == False):
        try:
            instance.profile.save()
            print("Profile Updated")
        except:
            Profile.objects.create(user=instance)
            print("Profile created for existing user.")
