from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from item.models import Item
from main.models import UserProfile
from .models import Order, Payment, Delivery, SupportTicket
from .forms import OrderForm, PaymentForm, DeliveryForm, SupportTicketForm
from .serializers import SupportTicketSerializer


@login_required
@api_view(['POST'])
def open_support_ticket(request):
    user = request.user

    if not user.is_superuser and not user.has_perm('auth.staff'):
        return Response({'error': 'You do not have permission to open a support ticket.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        serializer = SupportTicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@login_required
def create_support_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('support_ticket_list')
    else:
        form = SupportTicketForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/create_support_ticket.html', context)
    
@login_required
def update_support_ticket(request, pk):
    support_ticket = get_object_or_404(SupportTicket, pk=pk)

    if request.method == 'POST':
        form = SupportTicketForm(request.POST, instance=support_ticket)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('support_ticket_detail', pk=support_ticket.pk)
    else:
        form = SupportTicketForm(instance=support_ticket)

    context = {
        'form': form,
        'support_ticket': support_ticket,
    }
    return render(request, 'dashboard/update_support_ticket.html', context)

@login_required
def index(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    items = Item.objects.filter(created_by=request.user)
    orders = Order.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    deliveries = Delivery.objects.filter(order__in=orders)
    support_tickets = SupportTicket.objects.filter(user=request.user)

    return render(request, 'dashboard/index.html', {
        'user_profile': user_profile,
        'items': items,
        'orders': orders,
        'payments': payments,
        'deliveries': deliveries,
        'support_tickets': support_tickets,
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
@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OrderForm()
    
    return render(request, 'dashboard/create_order.html', {'form': form})
    
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm

@login_required
def update_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('order_detail', pk=pk)
    else:
        form = OrderForm(instance=order)
    
    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'dashboard/update_order.html', context)

@login_required
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('payment_list')
    else:
        form = PaymentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/create_payment.html', context)

@login_required
def update_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    
    context = {
        'form': form,
        'payment': payment,
    }
    return render(request, 'dashboard/update_payment.html', context)
    
@login_required
def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('delivery_list')
    else:
        form = DeliveryForm()

    context = {
        'form': form,
    }
    return render(request, 'dashboard/create_delivery.html', context)
    
@login_required
def update_delivery(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)

    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            # Redirect or render success message
            return redirect('delivery_list')
    else:
        form = DeliveryForm(instance=delivery)

    context = {
        'form': form,
        'delivery': delivery,
    }
    return render(request, 'dashboard/update_delivery.html', context)