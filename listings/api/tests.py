from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase

from api.models import House


class HouseTestCase(TestCase):
    """ Tests for House model. """

    def test_stringify(self):
        """ Test string representation of model. """
        # Given
        data = {
            "id": "1",
            "address": "Address 1",
            "city": "City 1",
            "state": "State 1",
            "zipcode": "Zipcode 1",
            }
        expected_result = (
            f"{data['id']} - {data['address']}, {data['city']}, "
            f"{data['state']}, {data['zipcode']}"
            )
        obj = House.objects.create(
            id=data["id"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zipcode=data["zipcode"],
            )

        # When
        result = str(obj)

        # Then
        self.assertEqual(result, expected_result)


class HouseViewSetTestCase(APITestCase):
    """ Tests for House view. """

    def test_get(self):
        """ Test GET method is available. """
        # Given
        url = reverse("house-list")

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """ Test POST method is not available. """
        # Given
        url = reverse("house-list")

        # When
        response = self.client.post(url)

        # Then
        self.assertEqual(response.status_code, 403)

    def test_put(self):
        """ Test PUT method is not available. """
        # Given
        url = reverse("house-list")

        # When
        response = self.client.put(url)

        # Then
        self.assertEqual(response.status_code, 403)

    def test_delete(self):
        """ Test PUT method is not available. """
        # Given
        url = reverse("house-list")

        # When
        response = self.client.delete(url)

        # Then
        self.assertEqual(response.status_code, 403)
