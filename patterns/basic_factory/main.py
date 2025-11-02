from factory import AutoFactory

factory = AutoFactory()

for car_name in ("Ford", "Holden", "Jeep"):
    car = factory.cars[car_name](make=car_name, model="Model X")
    print(car.start())
    print(car.stop())