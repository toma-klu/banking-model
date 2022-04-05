class Customer:
    def __init__(self, personal_id_nbr: str, name: str, surname: str, age: int) -> None:
        self.personal_id_nbr = personal_id_nbr
        self.name = name
        self.surname = surname
        self.age = age
        self.accounts: dict = {}

    def change_name(self, name: str) -> None:
        self.name = name

    def change_surname(self, surname: str) -> None:
        self.surname = surname

    def __repr__(self) -> str:
        account_str = ""
        for _, account in self.accounts.items():
            account_str += f"{account}\n\n"
        account_str = account_str.rstrip("\n")
        if account_str == "":
            account_str = "No accounts"
        return (
            f"PERSONAL INFORMATION:\n\n"
            f"Personal ID number: {self.personal_id_nbr}\n"
            f"Name: {self.name}\n"
            f"Surname: {self.surname}\n"
            f"Age: {self.age}\n\n"
            f"ACCOUNT INFORMATION:\n\n{account_str}"
        )
