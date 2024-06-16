from rest_framework import serializers
from .models import ParkingCard, ParkingLog

class ParkingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLog
        fields = ['id', 'parking_card', 'entry_time', 'exit_time', 'money', 'entry_image', 'exit_image']
