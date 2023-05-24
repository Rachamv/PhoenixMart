from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class MainTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user_profile = UserProfile.objects.create(user=self.user, first_name='John', last_name='Doe')

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.first_name, 'John')
        self.assertEqual(self.user_profile.last_name, 'Doe')

    def test_user_profile_str_representation(self):
        expected_str = f'{self.user.username} - {self.user_profile.first_name} {self.user_profile.last_name}'
        self.assertEqual(str(self.user_profile), expected_str)

    def test_user_profile_full_name_property(self):
        expected_full_name = f'{self.user_profile.first_name} {self.user_profile.last_name}'
        self.assertEqual(self.user_profile.full_name, expected_full_name)
