import requests
from external.schemas.weather_models import WeatherRequestParams, WeatherFcst
from typing import List
import xmltodict

BASE_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
service_key = "wQMVHtGXp9X3dziATpeU7zZAIWlDgzW1Ah3TE+kKZWqELsFbjo0tq4/FinbWGcMuIGMAsOplkak6WmY4viIM1Q=="

def get_weather_data(params: WeatherRequestParams) -> List[WeatherFcst]:
    request_params = params=params.to_params()
    request_params["serviceKey"] = service_key
    
    response = requests.get(BASE_URL, request_params)
    response.raise_for_status()

    response.headers.get("Content-Type")
    if(response.headers.get("Content-Type") != "application/xml"):
        return response.text
    else:
        data = response.json()

    return parse_weather_data(data)

def parse_weather_data(data: dict) -> List[WeatherFcst]:
    response = data.get("response", {})
    header = response.get("header", {})

    if(header.get("resultCode") != "00"):
        raise ValueError(f"API 응답 오류 : {header.get("resultMsg")}")

    items = response.get("body", {}).get("items", {}).get("item", [])
    return [WeatherFcst(**item) for item in items]