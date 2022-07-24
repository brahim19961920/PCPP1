from optparse import Values
import xml.etree.ElementTree


def main(xml_file="nyse.xml"):
    try:
        root = xml.etree.ElementTree.parse(xml_file).getroot()
    except FileNotFoundError:
        print(f"{xml_file} not found")
    except xml.etree.ElementTree.ParseError as e:
        print(f"Can not parse {xml_file}: {str(e)}")

    print(f'{"COMPANY".ljust(50)}{"LAST".ljust(40)}{"CHANGE".ljust(40)}{"MIN".ljust(40)}{"MAX".ljust(40)}')
    print(180 * "-")

    for quote in root.findall("quote"):
        line = quote.text.ljust(50)
        quote.attrib = quote.attrib

        line += quote.attrib["last"].ljust(40)
        line += quote.attrib["change"].ljust(40)
        line += quote.attrib["min"].ljust(40)
        line += quote.attrib["max"].ljust(40)

        print(line)
        line = ""

    print()


if __name__ == "__main__":
    main()
