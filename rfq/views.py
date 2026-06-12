from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import RequestForQuote
from .serializers import RequestForQuoteSerializer

class RFQCreateAPIView(generics.CreateAPIView):
    queryset = RequestForQuote.objects.all()
    serializer_class = RequestForQuoteSerializer
    permission_classes = [AllowAny]  # Allows anonymous visitors to submit RFQs