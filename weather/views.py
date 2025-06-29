from requests import Response
from django.db.models import CharField, F
from django.db.models.functions import Substr
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from common.utils.exceptions import CustomAPIException
from .models import *
from .serializers import *
from rest_framework import status

class AdminRegionViewSet(ModelViewSet):
    queryset = AdminRegion.objects.all()
    serializer_class = AdminRegionSerializer

    @action(detail=False, methods=['get'])
    def by_code(self, request):
        value = request.query_params.get('region_code')
        if not value:
            raise CustomAPIException(5001, "행정구역코드 없음(region_code)")
      # 기본 list 막기
    def list(self, request, *args, **kwargs):
        return Response({'detail': 'Not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # 기본 retrieve 막기
    def retrieve(self, request, *args, **kwargs):
        return Response({'detail': 'Not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # 필요하다면 create, update, destroy도 막을 수 있음
    def create(self, request, *args, **kwargs):
        return Response({'detail': 'Not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({'detail': 'Not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({'detail': 'Not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @action(detail=False, methods=["get"])
    def level_1(self, request):

        qs = self.queryset
        qs = qs.annotate(
            substr1=Substr(F('region_code'), 3, 8)
        ).filter(
            substr1='00000000'
        ).order_by('region_code')

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def level_2(self, request):
        param_value = request.query_params.get("region_code")

        if not param_value or not param_value.isdigit() or len(param_value) != 2:
            raise CustomAPIException(5001, "행정구역코드(region_code)가 올바르지 않습니다.")

        qs = self.queryset
        qs = qs.annotate(
            substr1=Substr(F('region_code'), 1, 2),
            substr2=Substr(F('region_code'), 3, 8),
            substr3=Substr(F('region_code'), 6, 5),
        ).filter(
            substr1=param_value,
        ).exclude(
            substr2='00000000'
        ).filter(
            substr3='00000',
        ).order_by('region_code')

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def level_3(self, request):
        param_value = request.query_params.get("region_code")

        if not param_value or not param_value.isdigit() or len(param_value) != 5:
            raise CustomAPIException(5001, "행정구역코드(region_code)가 올바르지 않습니다.")

        qs = self.queryset
        qs = qs.annotate(
            substr1=Substr(F('region_code'), 1, 5),
            substr2=Substr(F('region_code'), 3, 8),
        ).filter(
            substr1=param_value,
        ).exclude(
            substr2='00000000'
        ).order_by('region_code')

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
