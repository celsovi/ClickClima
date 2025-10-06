from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherData, SensorLocation
from .serializers import WeatherDataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny


class SensorDataView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]

    def put(self, request, sensor_id):
        try:
            location = SensorLocation.objects.get(id=sensor_id)
        except SensorLocation.DoesNotExist:
            return Response({"error": "Sensor not found"}, status=404)

        data = request.data.copy()
        data["location"] = location.id

        serializer = WeatherDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, sensor_id):
        data = WeatherData.objects.filter(location_id=sensor_id).order_by("-date_time").first()
        if not data:
            return Response({"error": "No data found"}, status=404)
        return Response(WeatherDataSerializer(data).data)

class SensorHistoryView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]
    
    def get(self, request, sensor_id):
        data = WeatherData.objects.filter(location_id=sensor_id).order_by("-date_time")
        return Response(WeatherDataSerializer(data, many=True).data)
