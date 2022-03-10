class BankingModel:
    def __init__(
        self, account_nbr, owner_name, owner_surname, balance=0, currency="EUR"
    ):
        self.account_nbr = account_nbr
        self.owner_name = owner_name
        self.owner_surname = owner_surname
        self.balance = balance
        self.currency = currency

    def change_owners_name(self, owner_name):
        self.owner_name = owner_name

    def change_owner_surname(self, owner_surname):
        self.owner_surname = owner_surname

    def change_currency(self, currency):
        self.currency = currency


class CreditCard(BankingModel):
    def __init__(
        self,
        account_nbr,
        owner_name,
        owner_surname,
        balance=0,
        currency="EUR",
        credit_limit=0,
    ):
        super().__init__(account_nbr, owner_name, owner_surname, balance, currency)
        self.credit_limit = credit_limit

    def change_credit_limit(self, credit_limit):
        self.credit_limit = credit_limit

    def __repr__(self):
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency}\n"
            f"Credit limit: {self.credit_limit} {self.currency}"
        )


class DebitCard(BankingModel):
    def __repr__(self):
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency}"
        )


credit_card_1 = CreditCard(
    account_nbr="LT000000001",
    owner_name="Jonas",
    owner_surname="Jonaitis",
    credit_limit=1000,
)
print(credit_card_1)
credit_card_1.owner_name
credit_card_1.change_owners_name("Jonukas")
credit_card_1.owner_name
credit_card_1.credit_limit
