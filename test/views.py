from dataclasses import asdict
import logging
from external.weather.client import WeatherAPIClient
from external.weather.schemas import ShortTermWeatherRequestParams
import requests
from rest_framework.decorators import api_view
from common.utils.exceptions import CustomAPIException

@api_view(['GET'])
def weather_api(request):
    logger = logging.getLogger(__name__)
    
    params = ShortTermWeatherRequestParams(**{
        "page_no": "1",
        "num_of_rows": "1000",
        "base_date": "20250617",
        "base_time": "0500",
        "nx": 37,
        "ny": 126
    })

    try:
        weather_api_client = WeatherAPIClient()
        weather_data = weather_api_client.get_short_term_weather(params)
        return [asdict(item) for item in weather_data]
        
    except requests.exceptions.RequestException as e:
        raise CustomAPIException(4000, f"날씨 데이터 조회 오류: {str(e)}")
    except ValueError as e:
        raise CustomAPIException(4001, f"날씨 데이터 조회 오류: {str(e)}")
    except Exception as e:
        raise CustomAPIException(4002, f"서버 내부 오류: {str(e)}")