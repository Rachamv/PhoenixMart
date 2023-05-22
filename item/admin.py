from django.contrib import admin

from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_sold')
    list_filter = ('category', 'is_sold')
    search_fields = ('name', 'category__name')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'description', 'price', 'image', 'is_sold')
        }),
        ('Additional Information', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
