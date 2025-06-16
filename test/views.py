import json
from django.shortcuts import render
import logging
from external.forcast.client import ForcastAPIClient
from external.forcast.schemas import ShortTermForcastRequestParams
import requests

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def forcast_api(request):
    logger = logging.getLogger(__name__)
    
    params = ShortTermForcastRequestParams(**{
        "page_no": "1",
        "num_of_rows": "1000",
        "base_date": "20250610",
        "base_time": "0500",
        "nx": 37,
        "ny": 126
    })

    try:
        forcast_api_client = ForcastAPIClient()
        weather_data = forcast_api_client.get_short_term_forcast(params)
        print(weather_data)
        return Response(weather_data)
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Weather API 요청 중 에러 발생: {str(e)}")
        return Response({"error": str(e)}, status=500)
    except ValueError as e:
        logger.error(f"JSON 파싱 중 에러 발생: {str(e)}")
        return Response({"error": json.loads(str(e))}, status=500)
    except Exception as e:
        logger.error(f"예상치 못한 에러 발생: {str(e)}")
        return Response({"error": "Internal server error"}, status=500)