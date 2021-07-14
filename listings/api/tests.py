from django.test import TestCase

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
