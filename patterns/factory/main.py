from factories import loader

for factory_name in ['ford_factory', 'holden_factory', 'jeep_factory']:
    factory = loader.load_factory(factory_name)
    car = factory.create_car()
    print(f"Created car: {car.name}, Start: {car.start()}, Stop: {car.stop()}")