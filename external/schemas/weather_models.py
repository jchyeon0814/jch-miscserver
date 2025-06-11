from dataclasses import dataclass
from typing import Optional

@dataclass
class WeatherRequestParams:
    serviceKey: str
    page_no: int = 1
    num_of_rows: int = 1000
    base_date: str
    base_time: str
    nx: int
    ny: int
    data_type: str = "JSON"

    def to_params(self) -> dict:
        return {
            "serviceKey": self.serviceKey,
            "pageNo": self.page_no,
            "numOfRows": self.num_of_rows,
            "base_date": self.base_date,
            "base_time": self.base_time,
            "nx": self.nx,
            "ny": self.ny,
            "dataType": self.data_type,
        }

@dataclass
class WeatherFcst:
    baseDate: str
    baseTime: str
    category: str
    fcstDate: str
    fcstTime: str
    fcstValue: str
    nx: int
    ny: int
