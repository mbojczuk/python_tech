from .car_factory import CarFactory
from cars.jeep import Jeep

class JeepFactory(CarFactory):

    def create_car(self) -> Jeep:
        self.jeep = jeep = Jeep()
        jeep.name = "Jeep Wrangler"
        return jeep