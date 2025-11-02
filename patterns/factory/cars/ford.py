from dataclasses import dataclass
from .car_base import CarBase

# Concrete implementations of different car types
@dataclass
class Ford(CarBase):
    def start(self) -> str:
        return f"{self.name} roars to life!"
    
    def stop(self) -> str:
        return f"{self.name} is stopping with traditional brakes."