from .car_factory import CarFactory
from cars.holden import Holden

class HoldenFactory(CarFactory):

    def create_car(self) -> Holden:
        self.holden = holden = Holden()
        holden.name = "Holden Commodore"
        return holden