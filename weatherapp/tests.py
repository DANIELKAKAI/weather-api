from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class WeatherApiTests(APITestCase):
    def test_location_temp(self):
        url = reverse("location-temp", kwargs={"city": "Nairobi"})
        response = self.client.get(url + "?days=8")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(data.get("maximum"))
        self.assertTrue(data.get("minimum"))
        self.assertTrue(data.get("median"))
        self.assertTrue(data.get("average"))

    def test_location_temp_invalid_days(self):
        url = reverse("location-temp", kwargs={"city": "Nairobi"})
        response = self.client.get(url + "?days=mon")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(data.get("error"))
