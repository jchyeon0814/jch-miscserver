from rest_framework import serializers
from .models import *

class AdminRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRegion
        fields = '__all__'
