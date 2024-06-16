from django.db import models

# Create your models here.
class ParkingCard(models.Model):
    card_number = models.CharField(primary_key=True, max_length=200)
    
class ParkingLog(models.Model):
    parking_card = models.ForeignKey(ParkingCard, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entry_image = models.ImageField(upload_to='images/entries/')
    exit_image = models.ImageField(upload_to='images/exits/', null=True, blank=True)
