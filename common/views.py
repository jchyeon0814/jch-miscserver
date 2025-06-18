from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class AdminRegionViewSet(ModelViewSet):
    queryset = AdminRegion.objects.all()
    serializer_class = AdminRegionSerializer
