from django.test import TestCase, Client
from django.test import TestCase, Client
from django.urls import reverse
from .models import Order, Payment, Delivery
from .forms import OrderForm, PaymentForm, DeliveryForm, ProfileForm

class DashboardAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Set up any necessary data for your tests

    def test_index_view(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')

        # Add more assertions to test the behavior of the index view
        # For example, check if the page contains expected content
        self.assertContains(response, "Welcome to your Dashboard")
        self.assertContains(response, "Order History")
        # Perform additional assertions as needed

    def test_update_profile_view(self):
        response = self.client.get(reverse('dashboard:update_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/profile.html')

        # Add more assertions to test the behavior of the update_profile view
        # For example, check if the form is rendered correctly
        self.assertIsInstance(response.context['form'], ProfileForm)
        self.assertContains(response, "<form")
        # Perform additional assertions as needed

