#!/usr/bin/env python


def main():
    account = BankAccount(123, 300)
    account.account_balance = 12
    account.deposit(120)
    account.deposit(1920000)

    try:
        account.account_balance = -10
    except BankException as e:
        print(e)

    try:
        account.account_number = 23
    except BankException as e:
        print(e)

    account.withdrawal(account.account_balance)
    print(account.account_balance)
    del account.account_number
    print(account.account_number)


class BankException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, account_balance):
        self.__account_number = account_number
        self.__account_balance = account_balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, *args, **kwargs):
        raise BankException("Operarion not permitted: change account number")

    @account_number.deleter
    def account_number(self):
        if self.__account_balance != 0:
            raise BankException("Operarion not permitted: delete account number. The account balance isn't null.")
        self.__account_number = None

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, new_balance):
        if new_balance < 0:
            raise BankException("Operarion not permitted: set a negative value as account balance")
        self.__account_balance = new_balance

    def deposit(self, amount):
        if amount > 100000:
            print(f"Deposit of an important amount {amount}")
        self.__account_balance += amount

    def withdrawal(self, amount):
        if amount > 100000:
            print(f"withdrawal of an important amount {amount}")
        self.__account_balance -= amount


if __name__ == "__main__":
    main()
