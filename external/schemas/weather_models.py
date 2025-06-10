from dataclasses import dataclass
from typing import Optional

@dataclass
class WeatherResponse:
    temperature: float
    description: str

    def from_api(data: dict) -> "WeatherResponse":
        return WeatherResponse(
            temperature=data['main']['temp'],
            description=data['weather'][0]['description']
        )

    def to_dict(self) -> dict:
        return {
            'temperature': self.temperature,
            'description': self.description
        }
