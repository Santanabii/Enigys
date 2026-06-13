from django.db import models

class RequestForQuote(models.Model):
    CLASSIFICATION_CHOICES = [
        ('epc', 'EPC Engineering & System Construction Layouts'),
        ('solar', 'Commercial & Industrial Solar Grid Transitions'),
        ('audit', 'Statutory EPRA Class A Investment Energy Audits'),
        ('medical', 'Medical Asset Management & Clinical Infrastructure'),
    ]

    company_name = models.CharField(max_length=255)
    representative_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES)
    scope_overview = models.TextField()
    compliance_confirmed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.company_name} - {self.classification}"

class Meta:
        verbose_name = "Request For Quote"
        verbose_name_plural = "Requests For Quotes"
        ordering = ['-submitted_at']