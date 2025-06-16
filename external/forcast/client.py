from typing import List

import requests
from external.forcast.endpoints import SHORT_TERM_FORCAST_URL
from miscserver import settings
from external.forcast.schemas import ShortTermForcastRequestParams, ShortTermForcast


class ForcastAPIClient:
    def __init__(self):
        self.service_key = settings.DATA_GO_KR_API_SERVICE_KEY

    def get_ultra_short_term_forcast(self, params: ShortTermForcastRequestParams) -> List[ShortTermForcast]:
        pass

    def get_short_term_forcast(self, params: ShortTermForcastRequestParams) -> List[ShortTermForcast]:
        request_params = params.to_params()
        data = self._request(SHORT_TERM_FORCAST_URL, request_params)
        items = self._parse_response(data)

        return [ShortTermForcast(**item) for item in items]


    def get_mid_term_forcast(self, params: ShortTermForcastRequestParams) -> List[ShortTermForcast]:
        pass

    def get_long_term_forcast(self, params: ShortTermForcastRequestParams) -> List[ShortTermForcast]:
        pass
    
    def _request(self, url: str, request_params: dict) -> List[ShortTermForcast]:
        request_params["serviceKey"] = self.service_key
        response = requests.get(url, request_params)
        response.raise_for_status()

        return response.json()
    
    def _parse_response(self, response_json: dict) -> List[ShortTermForcast]:
        response = response_json.get("response", {})
        header = response.get("header", {})

        if(header.get("resultCode") != "00"):
            raise ValueError(header)

        return response.get("body", {}).get("items", {}).get("item", [])

    




    
