from dataclasses import dataclass
from .car_base import CarBase

# Concrete implementations of different car types
@dataclass
class Holden(CarBase):
    def start(self) -> str:
        return f"{self.name} is starting silently."
    
    def stop(self) -> str:
        return f"{self.name} is stopping with regenerative braking."