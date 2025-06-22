from argparse import Action
from requests import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from common.utils.exceptions import CustomAPIException
from .models import *
from .serializers import *

class AdminRegionViewSet(ModelViewSet):
    queryset = AdminRegion.objects.all()
    serializer_class = AdminRegionSerializer

    @action(detail=False, methods=['get'])
    def by_code(self, request):
        value = request.query_params.get('region_code')
        if not value:
            raise CustomAPIException(5001, "행정구역코드 없음(region_code)")

        obj = AdminRegion.objects.get(region_code=value)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
    
