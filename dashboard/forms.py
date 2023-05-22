from django import forms
from .models import Order, Payment, Delivery
from item.models import Item
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=Item.objects.all())  # Update the field name to 'item'

    class Meta:
        model = Order
        fields = ('order_number', 'item', 'delivery_status', 'payment_status')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('amount', 'payment_date', 'payment_status')

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('delivery_date', 'delivery_address', 'tracking_number', 'delivery_status')
