from rest_framework import serializers
from .models import Mechanic

class MechanicSerializer(serializers.ModelSerializer):

    def validate_rating(self, value):

        if value < 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")

        return value

    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must contain exactly 10 digits.")

        return value

    class Meta:
        model = Mechanic
        fields = "__all__"
