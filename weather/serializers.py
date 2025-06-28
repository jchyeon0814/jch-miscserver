from rest_framework import serializers
from weather.models import AdminRegion

class AdminRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRegion
        fields = '__all__'
