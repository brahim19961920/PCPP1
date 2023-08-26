#! /usr/bin/env python

from random import uniform


def main():
    Apples().package_apples()


class Apples:
    max_number = 1000
    max_weight = 300

    def __init__(self):
        self.current_weight, self.current_apples_number = 0, 0

    def package_apples(self):
        print("Starting the packaging process")
        while self.max_number > self.current_apples_number and self.max_weight > self.current_weight:
            apple_weight = uniform(0.2, 0.5)
            if self.max_weight > self.current_weight + apple_weight:
                self.current_apples_number += 1
                self.current_weight += apple_weight
                print(self.current_apples_number, self.current_weight)
            else:
                print(
                    f"The packaging process has finished.\n{self.current_apples_number} apples have been packaged with a total weight of {self.current_weight} units."
                )
                return


if __name__ == "__main__":
    main()
