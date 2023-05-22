from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from main.models import UserProfile
from .models import Order, Payment, Delivery
from .forms import OrderForm, PaymentForm, DeliveryForm

@login_required
def index(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    items = Item.objects.filter(created_by=request.user)
    orders = Order.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    deliveries = Delivery.objects.filter(order__in=orders)

    return render(request, 'dashboard/index.html', {
        'user_profile': user_profile,
        'items': items,
        'orders': orders,
        'payments': payments,
        'deliveries': deliveries,
    })

@login_required
def update_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)

        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'dashboard/profile.html', {
        'form': form,
    })
