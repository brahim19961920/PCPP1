#!/usr/bin/env python

from abc import ABC, abstractmethod


def main():
    cheap_device = MFD1()
    cheap_device.scan_document()
    cheap_device.print_document()
    cheap_device.get_printer_status()
    cheap_device.get_scanner_status()

    medium_priced_device = MFD2()
    medium_priced_device.scan_document()
    medium_priced_device.print_document()
    medium_priced_device.get_printer_status()
    medium_priced_device.get_scanner_status()

    premium_device = MFD3()
    premium_device.scan_document()
    premium_device.print_document()
    premium_device.get_printer_status()
    premium_device.get_scanner_status()


class Scanner(ABC):
    def scan_document(self):
        print("The document has been scanned")

    @abstractmethod
    def get_scanner_status(self):
        pass


class Printer(ABC):
    def print_document(self):
        print("The document has been printed")

    @abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def __init__(self):
        self.price = 100
        self.resolution = 10

    def get_scanner_status(self):
        print("Cheap device")

    def get_printer_status(self):
        self.get_scanner_status()


class MFD2(Scanner, Printer):
    def __init__(self):
        self.price = 500
        self.resolution = 250

    def get_scanner_status(self):
        print("Medium priced device")

    def get_printer_status(self):
        self.get_scanner_status()


class MFD3(Scanner, Printer):
    def __init__(self):
        self.price = 1000
        self.resolution = 500

    def get_scanner_status(self):
        print("Premium device")

    def get_printer_status(self):
        self.get_scanner_status()


if __name__ == "__main__":
    main()
