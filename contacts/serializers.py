# contacts/serializers.py
from rest_framework import serializers
from .models import ContactInquiry

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ['id', 'name', 'company', 'email', 'phone', 'inquiry_type', 'message', 'created_at']