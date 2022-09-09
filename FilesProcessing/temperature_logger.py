#!/usr/bin/env python

import logging
from random import randint


def main():
    TemperatureLogger().generate_logs()


class TemperatureLogger:
    def __init__(self):
        self.logger = logging.getLogger("Temperature logs")
        logging.basicConfig(
            level=logging.DEBUG,
            filemode="w",
            filename="FilesProcessing/battery_temperature.log",
            format="%(levelname)s - TEMPERATURE_IN_CELSIUS %(message)s",
        )

    def generate_logs(self):
        for i in range(60):
            random_temperature = randint(15, 40)
            if random_temperature < 20:
                self.logger.debug(f"{str(random_temperature)} < 20")
            elif random_temperature > 35:
                self.logger.warning(f"{str(random_temperature)} > 35")
            else:
                self.logger.critical(f"19 <= {str(random_temperature)} <= 35")


if __name__ == "__main__":
    main()
