from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Category, Item

class ItemAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Test Description',
            price=10.99,
            created_by=self.user
        )

    def test_item_list_view(self):
        response = self.client.get(reverse('item:items'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.name)

    def test_item_detail_view(self):
        response = self.client.get(reverse('item:detail', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.name)
        self.assertContains(response, self.item.description)

    def test_new_item_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 200)

    def test_edit_item_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('item:edit', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_item_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('item:delete', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Item.objects.filter(pk=self.item.pk).exists())
