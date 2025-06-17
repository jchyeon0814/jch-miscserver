from dataclasses import asdict
from typing import List

import requests
from external.weather.endpoints import SHORT_TERM_WEATHER_URL
from miscserver import settings
from external.weather.schemas import ShortTermWeatherRequestParams, ShortTermWeather


class WeatherAPIClient:
    def __init__(self):
        self.service_key = settings.DATA_GO_KR_API_SERVICE_KEY

    def get_ultra_short_term_weather(self, params: ShortTermWeatherRequestParams) -> List[ShortTermWeather]:
        pass

    def get_short_term_weather(self, params: ShortTermWeatherRequestParams) -> List[ShortTermWeather]:
        request_params = params.to_params()
        
        data = self._request(SHORT_TERM_WEATHER_URL, request_params)
        
        items = self._parse_response(data)
        
        return [ShortTermWeather(**item) for item in items]

    def get_mid_term_weather(self, params: ShortTermWeatherRequestParams) -> List[ShortTermWeather]:
        pass

    def get_long_term_weather(self, params: ShortTermWeatherRequestParams) -> List[ShortTermWeather]:
        pass
    
    def _request(self, url: str, request_params: dict) -> List[ShortTermWeather]:
        request_params["serviceKey"] = self.service_key
        response = requests.get(url, request_params)
        response.raise_for_status()

        return response.json()
    
    def _parse_response(self, response_json: dict) -> List[ShortTermWeather]:
        response = response_json.get("response", {})
        header = response.get("header", {})

        if(header.get("resultCode") != "00"):
            raise ValueError(header.get("resultMsg"))

        return response.get("body", {}).get("items", {}).get("item", [])

    




    
