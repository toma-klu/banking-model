class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def change_name(self, name: str) -> None:
        self.name = name

    def change_surname(self, surname: str) -> None:
        self.surname = surname


class BankEmployee(Person):
    # Employee should be able to assist multiple customers
    pass


class BankCustomer(Person):
    # Customer should be able to have multiple accounts
    # Customer should have an assigned bank employee for assistance
    def __init__(self, personal_id_nbr: str, name: str, surname: str) -> None:
        Person.__init__(self, name, surname)
        self.personal_id_nbr = personal_id_nbr
