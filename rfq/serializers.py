from rest_framework import serializers
from .models import RequestForQuote

class RequestForQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForQuote
        fields = [
            'id', 
            'company_name', 
            'representative_name', 
            'email', 
            'phone', 
            'classification', 
            'scope_overview', 
            'compliance_confirmed', 
            'submitted_at'
        ]
        read_only_fields = ['id', 'submitted_at']