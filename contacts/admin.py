# contacts/admin.py
from django.contrib import admin
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'inquiry_type', 'company', 'created_at')
    list_filter = ('inquiry_type', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    
    # Simplified fieldsets - remove the problematic classes
    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Message', {
            'fields': ('inquiry_type', 'message')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )