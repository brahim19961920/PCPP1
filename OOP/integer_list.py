#!/usr/bin/env python


def main():
    l = IntegerList([1, 3])
    l += [1]
    l.append(12)
    l.extend([1, 3])
    l[0] = 0
    l.insert(0, -1)
    print(l)


class IntegerList(list):
    @staticmethod
    def check_element_type(value):
        if type(value) is not int:
            raise ValueError(f"{IntegerList.__name__}'s can only contain intgers.")

    def __setitem__(self, index, value):
        IntegerList.check_element_type(value)
        super().__setitem__(index, value)

    def __add__(self, iterable):
        for elt in iterable:
            IntegerList.check_element_type(elt)
        return super().__add__(iterable)

    def __iadd__(self, iterable):
        for elt in iterable:
            IntegerList.check_element_type(elt)
        return super().__iadd__(iterable)

    def insert(self, index, elt):
        IntegerList.check_element_type(elt)
        return super().insert(index, elt)

    def append(self, elt):
        IntegerList.check_element_type(elt)
        return super().append(elt)

    def extend(self, iterable):
        for elt in iterable:
            IntegerList.check_element_type(elt)
        return super().extend(iterable)


if __name__ == "__main__":
    main()
