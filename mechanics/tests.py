from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class MechanicAPITestCase(APITestCase):

    def test_get_mechanics_requires_authentication(self):
        response = self.client.get("/api/mechanics/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_create_mechanic(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.client.force_authenticate(user=user)

        data = {
            "name": "Raj Auto Care",
            "phone": "9876543210",
            "location": "Vadodara",
            "rating": 4.5,
            "is_open": True,
            "services": ["Oil Change", "Brake Repair"],
        }

        response = self.client.post(
            "/api/mechanics/",
            data,
            format="json",
        )

        print(response.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data["name"],
            "Raj Auto Care"
        )

    def test_create_mechanic_invalid_phone(self):
        user = User.objects.create_user(
            username="phoneuser",
            password="testpassword"
        )

        self.client.force_authenticate(user=user)

        data = {
            "name": "Raj Auto Care",
            "phone": "12345",
            "location": "Vadodara",
            "rating": 4.5,
            "is_open": True,
            "services": ["Oil Change", "Brake Repair"],
        }

        response = self.client.post(
            "/api/mechanics/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


    def test_create_mechanic_invalid_rating(self):
        user = User.objects.create_user(
            username="ratinguser",
            password="testpassword"
        )

        self.client.force_authenticate(user=user)

        data = {
            "name": "Raj Auto Care",
            "phone": "9876543210",
            "location": "Vadodara",
            "rating": 6,
            "is_open": True,
            "services": ["Oil Change", "Brake Repair"],
        }

        response = self.client.post(
            "/api/mechanics/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


    def test_create_mechanic_missing_required_field(self):
        user = User.objects.create_user(
            username="missinguser",
            password="testpassword"
        )

        self.client.force_authenticate(user=user)

        data = {
            "phone": "9876543210",
            "location": "Vadodara",
            "rating": 4.5,
            "is_open": True,
            "services": ["Oil Change", "Brake Repair"],
        }

        response = self.client.post(
            "/api/mechanics/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )