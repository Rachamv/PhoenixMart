from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    shipping_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Add any additional fields for the user profile

    def __str__(self):
        return self.user.username

# DRF Token model
class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = Token.objects.create(user=self.user).key
        return super(UserToken, self).save(*args, **kwargs)
