from .car_factory import CarFactory
from cars.ford import Ford

class FordFactory(CarFactory):

    def create_car(self) -> Ford:
        self.ford = ford = Ford()
        ford.name = "Ford Mustang"
        return ford 