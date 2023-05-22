from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from item.models import Item


class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified',)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)


class Ticket(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_tickets')
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
