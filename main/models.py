from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    shipping_address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    # Add any additional fields for the user profile

    def __str__(self):
        return self.user.username
