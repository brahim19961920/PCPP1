#!/usr/bin/env python

from csv import DictReader


def main():
    phone = Phone()
    phone.load_contacts_from_csv()
    for i in range(2):
        phone.search_contacts()


class PhoneContact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f"{self.name} ({self.number})"


class Phone:
    contacts = []

    def __init__(self, csv_file="FilesProcessing/contacts.csv"):
        self.csv_file_path = csv_file

    def load_contacts_from_csv(self):
        self.contacts = []

        with open(self.csv_file_path, newline="") as f:
            self.dict_reader = DictReader(f)

            for phone_contact in self.dict_reader:
                self.contacts.append(PhoneContact(phone_contact["Name"], phone_contact["Phone"]))

    def search_contacts(self):
        phrase = input("Search contacts: ")
        result = list(
            filter(
                lambda phone: phrase in repr(phone),
                self.contacts,
            )
        )

        if not result:
            print("No contact found")
            return

        for phone in result:
            print(phone)


if __name__ == "__main__":
    main()
