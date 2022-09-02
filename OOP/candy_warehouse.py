#!/usr/bin/env python

from copy import deepcopy, copy


def main():
    warehouse = [
        Delicacy(name="Lolly Pop", price=0.4, weight=133),
        Delicacy(name="Licorice", price=0.1, weight=251),
        Delicacy(name="Chocolate", price=1, weight=601),
        Delicacy(name="Sours", price=0.01, weight=513),
        Delicacy(name="Hard candies", price=0.3, weight=433),
    ]

    print("Source list of candies")
    for delicacy in warehouse:
        print(delicacy)

    warehouse_deep_copy = deepcopy(warehouse)
    for delicacy in warehouse_deep_copy:
        if delicacy.weight > 300:
            delicacy.price *= 0.8

    print("Price proposal with deepcopy")
    for delicacy in warehouse_deep_copy:
        print(delicacy)


class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, weight: {self.weight}"


if __name__ == "__main__":
    main()
