from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы








class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


