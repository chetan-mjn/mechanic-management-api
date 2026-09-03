from django.db import models

from mechanics.models import Mechanic

STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("IN_PROGRESS", "In Progress"),
    ("COMPLETED", "Completed"),
    ("CANCELLED", "Cancelled"),
]

class ServiceRequest(models.Model):

    customer_name = models.CharField(max_length=40)
    customer_phone = models.CharField(max_length=10)
    vehicle_number = models.CharField(max_length=10)
    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.CASCADE,
        related_name="service_requests"
    )
    service = models.CharField(max_length=30)
    problem_description = models.TextField(max_length=200)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="PENDING"
    )
    created_at = models.DateTimeField(auto_now_add=True)
