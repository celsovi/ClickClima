from django.urls import path
from .views import SensorDataView, SensorHistoryView

urlpatterns = [
    path('sensor/<int:sensor_id>', SensorDataView.as_view()),
    path('sensor/<int:sensor_id>/historical', SensorHistoryView.as_view()),
]
