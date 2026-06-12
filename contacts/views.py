# contacts/views.py
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import ContactInquiry
from .serializers import ContactInquirySerializer

class ContactCreateAPIView(CreateAPIView):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
    permission_classes = [AllowAny] # Gives unauthenticated guests permission to mail the team