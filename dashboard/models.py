from django.contrib.auth.models import User
from django.db import models
from item.models import Item


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

