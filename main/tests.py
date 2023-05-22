from django.test import TestCase, Client
from django.urls import reverse
from .models import UserProfile

class MainAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a user and user profile
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.create(
            user=self.user, 
            shipping_address='Test Address', 
            contact_number='123456789'
            )

    def test_index_view(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        
        # Check if the user profile is passed to the template context
        self.assertIn('user_profile', response.context)
        self.assertEqual(response.context['user_profile'], self.user_profile)
        
        # Add more assertions to test the behavior of the index view
        # For example, check if the items are passed to the template context
        self.assertIn('items', response.context)
        # Perform additional assertions as needed

    def test_contact_view(self):
            response = self.client.get(reverse('main:contact'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'main/contact.html')

            # Add more assertions to test the behavior of the contact view
            # For example, check if the page contains expected content
            self.assertContains(response, "Contact Us")
            self.assertContains(response, "Email: contact@example.com")
            # Perform additional assertions as needed