#!/usr/bin/env python

import configparser
from os import chdir


def main():
    chdir("FilesProcessing")
    conf_file = configparser.ConfigParser()
    conf_file.read("mess.ini")
    dev_conf = configparser.ConfigParser()
    prod_conf = configparser.ConfigParser()

    for section in conf_file.sections():
        if conf_file[section].get("env") == "prod":
            prod_conf[section] = conf_file[section]
            del prod_conf[section]["env"]
        else:
            dev_conf[section] = conf_file[section]
            del dev_conf[section]["env"]

    with open("prod_config.ini", "w") as prod_file:
        prod_conf.write(prod_file)

    with open("dev_config.ini", "w") as dev_file:
        dev_conf.write(dev_file)


if __name__ == "__main__":
    main()
