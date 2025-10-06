from django.db import models


class SensorLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    location = models.ForeignKey(SensorLocation, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    luminosity = models.FloatField(null=True, blank=True)
    uv = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    noise = models.FloatField(null=True, blank=True)
    eCO2 = models.FloatField(null=True, blank=True)
    VOC = models.FloatField(null=True, blank=True)
    pm1 = models.FloatField(null=True, blank=True)
    pm25 = models.FloatField(null=True, blank=True)
    pm10 = models.FloatField(null=True, blank=True)
