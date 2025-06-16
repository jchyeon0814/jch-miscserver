from dataclasses import dataclass
from typing import Optional

@dataclass
class ShortTermForcastRequestParams:
    base_date: str
    base_time: str
    nx: int
    ny: int
    page_no: int = 1
    num_of_rows: int = 1000
    data_type: str = "JSON"

    def to_params(self) -> dict:
        return {
            "pageNo": self.page_no,
            "numOfRows": self.num_of_rows,
            "base_date": self.base_date,
            "base_time": self.base_time,
            "nx": self.nx,
            "ny": self.ny,
            "dataType": self.data_type,
        }

@dataclass
class ShortTermForcast:
    baseDate: str
    baseTime: str
    category: str
    fcstDate: str
    fcstTime: str
    fcstValue: str
    nx: int
    ny: int
