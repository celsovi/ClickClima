from django.test import TestCase
# sensors/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SensorLocation, WeatherData

class SensorAPITests(APITestCase):
    def setUp(self):
        self.sensor = SensorLocation.objects.create(
            name="Sensor Teste",
            latitude=-23.55,
            longitude=-46.63
        )
        self.put_url = f"/api/sensor/{self.sensor.id}"
        self.historical_url = f"/api/sensor/{self.sensor.id}/historical"

        self.payload = {
            "temperature": 25.3,
            "humidity": 60.1,
            "pressure": 1.01,
            "altitude": 760,
            "luminosity": 450,
            "uv": 3.2,
            "noise": 45.0,
            "eCO2": 550,
            "VOC": 120,
            "pm1": 10.0,
            "pm25": 14.3,
            "pm10": 20.8
        }

    def test_put_sensor_data(self):
        """Testa envio de dados de um sensor via PUT"""
        response = self.client.put(self.put_url, self.payload, format='json')
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WeatherData.objects.count(), 1)
        self.assertEqual(WeatherData.objects.first().temperature, self.payload["temperature"])

    def test_get_historical_data(self):
        """Testa retorno do histórico após envio de dados"""
        # Primeiro insere um dado
        self.client.put(self.put_url, self.payload, format='json')

        # Depois requisita o histórico
        response = self.client.get(self.historical_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["temperature"], self.payload["temperature"])
