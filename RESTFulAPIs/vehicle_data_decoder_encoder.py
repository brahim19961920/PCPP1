#!/usr/bin/env python

import json


def main():
    user_input = input(
        """What can I do for you?\n1 - Produce a JSON string describing a vehicle\n2 - Decode a JSON string into vehicle data\n""",
    )

    if not user_input.isdigit() and int(user_input) not in [1, 2]:
        print(f"Invalid choice {user_input}")
        exit(-1)

    elif user_input == "1":
        reg = input("Registration number: ")
        year_of_prod = input("Year of production: ")
        passenger = input("Passenger [y/n]: ")
        vehicle_mass = input("Vahicle mass: ")
        print(json.dumps(Vehicle(reg, year_of_prod, passenger, vehicle_mass), cls=Encoder))

    else:
        str_json = input("Entre Vehicle JSON string: ")
        print(json.loads(str_json, cls=Decoder).__dict__)


class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass


class Encoder(json.JSONEncoder):
    def default(self, v):
        if isinstance(v, Vehicle):
            return v.__dict__
        return super().default(v)


class Decoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)


if __name__ == "__main__":
    main()
