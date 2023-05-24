from django.contrib import admin
from .models import SupportTicket, UserProfile

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user', 'opened_by', 'resolved', 'status', 'created_at', 'closed_at']
    list_filter = ['resolved', 'status']
    search_fields = ['subject', 'user__username']
    readonly_fields = ['created_at', 'closed_at']
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True, closed_at=timezone.now())
    mark_resolved.short_description = "Mark selected tickets as resolved"

admin.site.register(SupportTicket, SupportTicketAdmin)


# Unregister UserProfile model if it's already registered
if admin.site.is_registered(UserProfile):
    admin.site.unregister(UserProfile)
    class UserProfileAdmin(admin.ModelAdmin):
        list_display = ('user', 'bio')

    admin.site.register(UserProfile, UserProfileAdmin)
