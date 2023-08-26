#!/usr/bin/env python


def main():
    t1 = TimeInterval(hours=21, minutes=58, seconds=50)
    t2 = TimeInterval(hours=1, minutes=45, seconds=22)
    t3 = t1 + t2
    t4 = t1 - t2
    t5 = t1 * 2
    t6 = t1 + 234
    t7 = t1 - 51
    print(t3)
    print(t4)
    print(t5)
    print(t6)
    print(t7)


class TimeInterval:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise TypeError(f"Invalid {key} parameter:{value}. Its type must be int.")
            if key not in ["hours", "minutes", "seconds"]:
                raise AssertionError(f"Invalid keyword parameter {key}")

        self.hours = kwargs.get("hours", 0)
        self.minutes = kwargs.get("minutes", 0)
        self.seconds = kwargs.get("seconds", 0)

    def get_time_in_seconds(self):
        return self.seconds + 60 * self.minutes + 3600 * self.hours

    def get_time_from_seconds(self, time_in_seconds):
        hours = time_in_seconds // 3600
        minutes = (time_in_seconds - hours * 3600) // 60
        seconds = (time_in_seconds - hours * 3600 - minutes * 60) % 3600
        return hours, minutes, seconds

    def __add__(self, other):
        hours, minutes, seconds = self.get_time_from_seconds(
            self.get_time_in_seconds() + (other if isinstance(other, int) else other.get_time_in_seconds())
        )
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __sub__(self, other):
        hours, minutes, seconds = self.get_time_from_seconds(
            self.get_time_in_seconds() - (other if isinstance(other, int) else other.get_time_in_seconds())
        )
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __mul__(self, number):
        hours, minutes, seconds = self.get_time_from_seconds(self.get_time_in_seconds() * number)
        return TimeInterval(hours=hours, minutes=minutes, seconds=seconds)

    def __str__(self):
        return f"{str(self.hours)}:{str(self.minutes)}:{str(self.seconds)}"


if __name__ == "__main__":
    main()
