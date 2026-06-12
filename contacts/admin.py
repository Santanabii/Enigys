# contacts/admin.py
from django.contrib import admin
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    # Columns displayed directly in the dashboard list view
    list_display = ('name', 'email', 'inquiry_type', 'company', 'created_at')
    
    # Right-hand sidebar filter panels for quick sorting
    list_filter = ('inquiry_type', 'created_at')
    
    # Active search omnibar targeting key data values
    search_fields = ('name', 'email', 'company', 'message')
    
    # Keeps timestamps safe from manual tampering inside the detail panel
    readonly_fields = ('created_at',)
    
    # Groups the data cleanly when you click into an individual message
    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Message Payload', {
            'fields': ('inquiry_type', 'message')
        }),
        ('System Metadata', {
            'fields': ('created_at',),  # FIXED: Use 'created_at' instead of 'readonly_fields'
            'classes': ('collapse',), 
        }),
    )