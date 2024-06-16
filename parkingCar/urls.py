from django.urls import path
from .views import CardLogView

urlpatterns = [
    path('cardlog', CardLogView.as_view(), name='cardlog'),
]
