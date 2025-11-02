from dataclasses import dataclass
from .car_base import CarBase

# Concrete implementations of different car types
@dataclass
class Jeep(CarBase):
    def start(self) -> str:
        return f"{self.make} {self.model} rumbles on."
    
    def stop(self) -> str:
        return f"{self.make} {self.model} is stopping with off-road brakes."