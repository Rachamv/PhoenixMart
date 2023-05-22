from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Item
from .models import Conversation, ConversationMessage

class ConversationAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.item = Item.objects.create(name='Test Item', created_by=self.user)
        self.conversation = Conversation.objects.create(item=self.item)
        self.conversation.members.add(self.user)
        self.message = ConversationMessage.objects.create(conversation=self.conversation, content='Test message', created_by=self.user)

    def test_new_conversation_view(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('conversation:new_conversation', args=[self.item.pk]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the behavior of the new_conversation view

    def test_inbox_view(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('conversation:inbox'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the behavior of the inbox view

    def test_detail_view(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('conversation:detail', args=[self.conversation.pk]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions to test the behavior of the detail view

    # Add more test methods to cover other views and functionalities in the conversation app
