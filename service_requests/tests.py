from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from mechanics.models import Mechanic


class ServiceRequestAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.client.force_authenticate(user=self.user)

        self.mechanic = Mechanic.objects.create(
            name="Raj Auto Care",
            phone="9876543210",
            location="Vadodara",
            rating=4.5,
            is_open=True,
            services=["Oil Change", "Brake Repair"]
        )

    def test_create_service_request(self):
        data = {
            "customer_name": "Chetan",
            "customer_phone": "0987654321",
            "vehicle_number": "GJ06AB1234",
            "mechanic": self.mechanic.id,
            "service": "Oil Change",
            "problem_description": "Engine oil needs replacement"
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data["status"],
            "PENDING"
        )

    def test_invalid_vehicle_number(self):
        data = {
            "customer_name": "Chetan",
            "customer_phone": "0987654321",
            "vehicle_number": "INVALID123",
            "mechanic": self.mechanic.id,
            "service": "Oil Change",
            "problem_description": "Engine problem"
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_service_not_offered_by_mechanic(self):
        data = {
            "customer_name": "Chetan",
            "customer_phone": "0987654321",
            "vehicle_number": "GJ06AB1234",
            "mechanic": self.mechanic.id,
            "service": "AC Repair",
            "problem_description": "AC is not working"
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_nonexistent_mechanic(self):
        data = {
            "customer_name": "Chetan",
            "customer_phone": "0987654321",
            "vehicle_number": "GJ06AB1234",
            "mechanic": 9999,
            "service": "Oil Change",
            "problem_description": "Engine problem"
        }

        response = self.client.post(
            "/api/service-requests/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )