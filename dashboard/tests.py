from django.test import TestCase
from django.contrib.auth.models import User
from item.models import Item
from main.models import UserProfile
from .models import Order, Payment, Delivery
from .forms import OrderForm, PaymentForm, DeliveryForm

class DashboardTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.item = Item.objects.create(name='Test Item', created_by=self.user)
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.order = Order.objects.create(order_number='12345', user=self.user, product=self.item, delivery_status='Pending', payment_status='Pending')
        self.payment = Payment.objects.create(amount='100.00', payment_date='2023-05-15', user=self.user, payment_status='Paid')
        self.delivery = Delivery.objects.create(delivery_date='2023-05-15', delivery_address='Test Address', tracking_number='123456', delivery_status='Delivered', order=self.order)

    def test_order_form(self):
        form_data = {
            'order_number': '54321',
            'product': self.item.id,
            'delivery_status': 'Delivered',
            'payment_status': 'Paid'
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_payment_form(self):
        form_data = {
            'amount': '50.00',
            'payment_date': '2023-05-16',
            'payment_status': 'Pending'
        }
        form = PaymentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_delivery_form(self):
        form_data = {
            'delivery_date': '2023-05-16',
            'delivery_address': 'Test Address 2',
            'tracking_number': '654321',
            'delivery_status': 'Pending'
        }
        form = DeliveryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dashboard_index(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')
        self.assertContains(response, 'Test Item')

    def test_dashboard_update_profile(self):
        self.client.force_login(self.user)
        response = self.client.get('/dashboard/update-profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/profile.html')

        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
        }
        response = self.client.post('/dashboard/update-profile/', data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dashboard/')
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.email, 'test@example.com')

