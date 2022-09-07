#!/usr/bin/env python

from os import chdir
import xml.etree.ElementTree as ET


def main():
    chdir("FilesProcessing")
    root = ET.Element("Shop")
    category_element = ET.SubElement(root, "category")

    for product in [
        {
            "name": "Good Morning Sunshine",
            "attr": {"type": "cereals", "producer": "OpenEDG Testing Service", "price": "9.90", "currency": "USD"},
        },
        {
            "name": "GSpaghetti Veganietto",
            "attr": {"type": "pasta", "producer": "Programmers Eat Pasta", "price": "15.49", "currency": "EUR"},
        },
        {
            "name": "Fantastic Almond Milk",
            "attr": {"type": "beverages", "producer": "Drinks4Coders Inc.", "price": "19.75", "currency": "USD"},
        },
    ]:
        product_element = ET.SubElement(category_element, "product", {"name": product["name"]})
        for tag, text in product["attr"].items():
            sub_element = ET.SubElement(product_element, tag)
            sub_element.text = text

    tree = ET.ElementTree(root)
    tree.write("shop.xml", "UTF-8", True)


if __name__ == "__main__":
    main()
