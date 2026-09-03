from rest_framework import viewsets
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from rest_framework.permissions import IsAuthenticated

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [IsAuthenticated]