import requests
from external.schemas.weather_models import WeatherRequestParams, WeatherFcst
from typing import List

BASE_URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

def get_weather_data(params: WeatherRequestParams) -> List[WeatherFcst]:
    response = requests.get(BASE_URL, params=params.to_params())
    response.raise_for_status()
    data = response.json()
    return data['response']['body']['items']['item']