#!/usr/bin/env python

import json
import logging
import requests
import json

SERVER_URL = "http://localhost:3000/cars/"


def main():
    while True:
        if not check_server():
            print("Server is not responding - quitting!")
            exit(1)
            
        print_menu()
        choice = read_user_choice()
        
        if choice == "0":
            print("Bye!")
            exit(0)
        elif choice == "1":
            list_cars()
        elif choice == "2":
            add_car()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            update_car()


def check_server(cid=None):
    try:
        url = f"{SERVER_URL}{cid if cid is not None else ''}"
        r = requests.get(url)
        return r.status_code == requests.codes.ok
    except:
        return False


def print_menu():
    print(
        """
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
"""
    )


def read_user_choice():
    user_choice = input("Enter your choice (0..4)\n")
    if user_choice.isdigit() and int(user_choice) in range(5):
        return user_choice

    logging.error(f"Invalid choice {user_choice}")
    return False


def print_header():
    for property in ["id", "brand", "model", "production_year", "convertible"]:
        print(property.ljust(20), end="| ")
    print()



def print_car(car):
    for value in car.values():
        print(str(value).ljust(20), end="|")
    print()


def list_cars():
    r = requests.get(SERVER_URL)
    if not r.text:
        logging.error("*** Database is empty ***")
    print_header()
    for car in r.json():
        print_car(car)


def name_is_valid(name):
    if not isinstance(name, str):
        return False
    if not len(name):
        return False
    return name.isalnum()


def enter_id():
    id = input("Car ID (empty string to exit):")
    if not id:
        return None
    if not id.isdigit():
        return None
    return int(id)


def enter_production_year():
    production_year = input("Car production year (empty string to exit):")
    if not production_year:
        return None
    if production_year.isdigit() and int(production_year) in range(1900, 2001):
        return int(production_year)
    return None


def enter_name(what):
    name = input(f"Car {what} (empty string to exit):")
    if name_is_valid(name):
        return name
    return None


def enter_convertible():
    convertible = input("Is this car convertible? [y/n] (empty string to exit):")
    if not convertible:
        return None
    if convertible.upper() == "Y":
        return True
    return False


def delete_car():
    id = enter_id()
    if id is not None:
        r = requests.delete(f"{SERVER_URL}{id}")
        if r.status_code != requests.codes.ok:
            logging.error(f"Failed to delete car with id {id}")


def input_car_data():
    id = enter_id()
    if id is None:
        return None
    brand = enter_name("brand")
    if brand is None:
        return None
    model = enter_name("model")
    if model is None:
        return None
    production_year = enter_production_year()
    if production_year is None:
        return None
    convertible = enter_convertible()
    if convertible is None:
        return None
    return {"id": id, "brand": brand, "model": model, "prodcution_year": production_year, "convertible": convertible}


def add_car():
    car_data = input_car_data()
    if car_data is not None:
        r = requests.post(f"{SERVER_URL}", headers={"Content-Type": "application/json"}, data=json.dumps(car_data))
        if r.status_code != r.status_code.created:
            logging.error("Failed to add a new car")


def update_car():
    car_data = input_car_data()
    if car_data is not None:
        r = requests.put(
            f"{SERVER_URL}/{car_data['id']}", headers={"Content-Type": "application/json"}, data=json.dumps(car_data)
        )
        if r.status_code != 201:
            logging.error("Failed to add update car")


if __name__ == "__main__":
    main()
