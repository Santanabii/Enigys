# contacts/models.py
from django.db import models

class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    inquiry_type = models.CharField(max_length=100) # General, Support, Careers, etc.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']

def __str__(self):
        return f"{self.name} - {self.inquiry_type}"  