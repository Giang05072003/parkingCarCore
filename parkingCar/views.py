from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import ParkingCard, ParkingLog
from .serializers import ParkingLogSerializer

class CardLogView(APIView):
    def post(self, request):
        serializer = ParkingLogSerializer(data=request.data)
        
        if serializer.is_valid():
            card_number = request.data.get('parking_card')
            try:
                parking_card = ParkingCard.objects.get(card_number=card_number)
            except ParkingCard.DoesNotExist:
                return Response({"mess": f"Parking card with number '{card_number}' does not exist."},
                                status=status.HTTP_404_NOT_FOUND)
            
            parking_log = ParkingLog.objects.filter(parking_card=parking_card, exit_time__isnull=True).first()

            if parking_log:
                parking_log.exit_time = timezone.now()
                duration = parking_log.exit_time - parking_log.entry_time
                hours = duration.total_seconds() / 3600

                if hours < 12:
                    parking_log.money = 3000
                else:
                    parking_log.money = 5000

                parking_log.exit_image = request.FILES['exit_image']
                parking_log.save()
                updated_serializer = ParkingLogSerializer(parking_log)
                return Response(updated_serializer.data, status=status.HTTP_200_OK)
            else:
                parking_log = ParkingLog(
                    parking_card = parking_card,
                    entry_image = request.FILES['entry_image'],
                )
                parking_log.save()
                response_serializer = ParkingLogSerializer(parking_log)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        logs = ParkingLog.objects.all()
        serializer = ParkingLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
