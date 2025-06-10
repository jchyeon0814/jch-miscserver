from django.shortcuts import render
import requests
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def weather_api(request):
    logger = logging.getLogger(__name__)
    
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
    service_key = "wQMVHtGXp9X3dziATpeU7zZAIWlDgzW1Ah3TE+kKZWqELsFbjo0tq4/FinbWGcMuIGMAsOplkak6WmY4viIM1Q=="
    # service_key를 직접 사용하고 requests.utils.quote() 제거
    
    params = {
        "ServiceKey": service_key,
        "dataType": "JSON",
        "pageNo": "1",
        "numOfRows": "1000",
        "base_date": "20250610",
        "base_time": "0500",
        "nx": "37",
        "ny": "126"
    }

    try:
        session = requests.Session()
        response = session.get(url, params=params)

        response.raise_for_status()  # HTTP 에러 체크

        weather_data = response.json()
        logger.info(f"Weather API 응답 데이터: {weather_data}")
        
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