from django.contrib import admin
from .models import RequestForQuote

@admin.register(RequestForQuote)
class RequestForQuoteAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'representative_name', 'email', 'classification', 'submitted_at')
    list_filter = ('classification', 'submitted_at', 'compliance_confirmed')
    search_fields = ('company_name', 'representative_name', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    
    fieldsets = (
        ('Company Information', {
            'fields': ('company_name', 'representative_name', 'email', 'phone')
        }),
        ('Request Details', {
            'fields': ('classification', 'scope_overview', 'compliance_confirmed')
        }),
        ('Submission Metadata', {
            'fields': ('submitted_at',)
        }),
    )
