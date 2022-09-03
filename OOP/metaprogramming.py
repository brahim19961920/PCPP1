#!/usr/bin/env python

from datetime import datetime


def main():
    p = Person("Brahim", 26)
    c = City("Cannes", "06")

    print(MetaClass.instansiated_class)

    for cls in MetaClass.instansiated_class:
        print(cls.get_instantiation_time())


class MetaClass(type):
    instansiated_class = []

    def __new__(mcs, name, bases, attributes):
        obj = super().__new__(mcs, name, bases, attributes)
        obj.instantiation_time = datetime.now()

        if "get_instantiation_time" not in attributes:
            obj.get_instantiation_time = lambda: str(obj.instantiation_time)

        mcs.instansiated_class.append(obj)
        return obj


class Person(metaclass=MetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class City(metaclass=MetaClass):
    def __init__(self, name, departement):
        self.name = name
        self.departement = departement


if __name__ == "__main__":
    main()
