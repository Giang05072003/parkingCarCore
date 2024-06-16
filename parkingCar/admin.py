from django.contrib import admin
from .models import ParkingCard, ParkingLog

admin.site.register(ParkingCard)
admin.site.register(ParkingLog)
