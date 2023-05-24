from django.contrib.auth.models import User
from django.db import models
from item.models import Item
from main.models import UserProfile
from conversation.models import Conversation


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50)


class Delivery(models.Model):
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=200)
    tracking_number = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Inbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversations = models.ManyToManyField(Conversation)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()



class SupportTicket(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opened_by = models.ForeignKey(User, related_name='opened_tickets', on_delete=models.SET_NULL, null=True)
    resolved_by = models.ForeignKey(User, related_name='resolved_tickets', on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    closed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    @property
    def can_open_ticket(self):
        return self.user.is_superuser or self.user.is_staff