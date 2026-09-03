from rest_framework import serializers
from .models import ServiceRequest
import re

class ServiceRequestSerializer(serializers.ModelSerializer):

    def validate_vehicle_number(self, value):
        pattern = r"^[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}$"

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Invalid vahicle number format. Example: GJ06AB1234"
            )

        return value

    def validate(self, data):
        mechanic = data["mechanic"]
        service = data["service"]

        if service not in mechanic.services:
            raise serializers.ValidationError("This mechanice does not offer this service.")

        return data

    def validate_customer_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value

    class Meta:
        model = ServiceRequest
        fields = "__all__"
        read_only_fields = ["status", "created_at"]