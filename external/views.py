from django.http import HttpResponse
from django.shortcuts import render
import requests
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response

from external.services import weather_services
from external.schemas.weather_models import WeatherRequestParams

@api_view(['GET'])
def weather_api(request):
    logger = logging.getLogger(__name__)
    
    params = WeatherRequestParams(**{
        "page_no": "1",
        "num_of_rows": "1000",
        "base_date": "20250610",
        "base_time": "0500",
        "nx": 37,
        "ny": 126
    })

    try:
        weather_data =weather_services.get_weather_data(params)
        print(weather_data)
        return Response(weather_data)
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Weather API 요청 중 에러 발생: {str(e)}")
        return Response({"error": str(e)}, status=500)
    except ValueError as e:
        logger.error(f"JSON 파싱 중 에러 발생: {str(e)}")
        return Response({"error": "Invalid JSON response"}, status=500)
    except Exception as e:
        logger.error(f"예상치 못한 에러 발생: {str(e)}")
        return Response({"error": "Internal server error"}, status=500)