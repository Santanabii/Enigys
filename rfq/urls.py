from django.urls import path
from .views import RFQCreateAPIView

urlpatterns = [
    path('submit/', RFQCreateAPIView.as_view(), name='rfq-submit'),
]