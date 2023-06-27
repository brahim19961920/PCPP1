#!/usr/bin/env python

from os import chdir
import xml.etree.ElementTree as ET


def main():
    TC = ForecastXmlParser().parse()


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature):
        return round(9 / 5 * temperature + 32, 1)


class ForecastXmlParser:
    def __init__(self, xml_file_name="forecast.xml"):
        chdir("FilesProcessing")
        self.root = ET.parse(xml_file_name).getroot()
        self.temperature_converter = TemperatureConverter()

    def parse(self):
        for element in self.root:
            print(
                f"{element[0].text} {element[1].text} Celsius, {self.temperature_converter.convert_celsius_to_fahrenheit(float(element[1].text))} Fahrenheit"
            )


if __name__ == "__main__":
    main()
