#!/usr/bin/env python
from datetime import datetime


def main():
    sum_function(1, 2, b=3)


def decorator(function):
    def wrapper(*args, **kwargs):
        print(f"{str(datetime.now().today())}:Result of {function.__name__} {function(*args, **kwargs)}")

    return wrapper


@decorator
def sum_function(*args, **kwargs):
    res = 0
    for n in list(args) + list(kwargs.values()):
        res += n
    return res


if __name__ == "__main__":
    main()
