from django.contrib import admin
from .models import Conversation, ConversationMessage, Ticket

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'created', 'modified')
    list_filter = ('created', 'modified')
    search_fields = ('item__name', 'members__username')

@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'content', 'created', 'created_by')
    list_filter = ('created',)
    search_fields = ('conversation__item__name', 'content', 'created_by__username')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'seller', 'subject', 'created_at', 'resolved')
    list_filter = ('created_at', 'resolved')
    search_fields = ('buyer__username', 'seller__username', 'subject')
