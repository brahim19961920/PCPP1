#!/usr/bin/env python


def main():
    engine1 = Engine("electric")
    engine2 = Engine("petrol")

    city_tires = [Tire(15), Tire(15)]
    off_road_tires = [Tire(18), Tire(18)]

    city_car = Vehicle(1, engine1, city_tires)
    print("City car actions")
    print()
    city_car.engine.start()
    city_car.engine.stop()
    city_car.engine.get_state()
    for tire in city_car.tires:
        tire.pump(2)

    for tire in city_car.tires:
        tire.get_pressure()

    print()

    all_terrain_car = Vehicle(2, engine2, off_road_tires)
    print("All terain car")
    print()

    all_terrain_car.engine.get_state()
    for tire in all_terrain_car.tires:
        tire.get_pressure()


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


class Engine:
    def __init__(self, fuel):
        self.fuel = fuel
        self.state = "stopped"

    def start(self):
        if self.state == "stopped":
            print("Statring the engine")
            self.state = "started"
        else:
            print("Enging already started")

    def stop(self):
        if self.state == "started":
            print("Stopping the engine")
            self.state = "stopped"
        else:
            print("Enging already stopped")

    def get_state(self):
        print(f"Engine state: {self.state}")


class Tire:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def get_pressure(self):
        print(f"Tire pressure {self.pressure}")

    def pump(self, pressure_amount):
        if pressure_amount < 0:
            raise Exception("Cannot pump the tire with a negative amount")

        print(f"Increasing tires pressure by {pressure_amount}")
        self.pressure += pressure_amount


if __name__ == "__main__":
    main()
