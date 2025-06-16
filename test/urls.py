from django.urls import path
from .views import forcast_api

urlpatterns = [
    path('api/forcast/', forcast_api),
]