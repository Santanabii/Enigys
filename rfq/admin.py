from django.contrib import admin
from .models import RequestForQuote

@admin.register(RequestForQuote)
class RequestForQuoteAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'classification', 'submitted_at')