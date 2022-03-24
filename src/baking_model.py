import calendar
from datetime import date

# Exchange rate from EUR (1 EUR)
EXCHANGE_RATES = {"EUR": 1.0000, "USD": 1.0952, "GBP": 0.8420}


class BankingModel:
    pass


class RegisterCardAccount:
    def __init__(
        self, account_nbr, owner_name, owner_surname, balance=0, currency="EUR"
    ):
        self.account_nbr = account_nbr
        self.owner_name = owner_name
        self.owner_surname = owner_surname
        self.balance = balance
        self.currency = currency

    def change_owner_name(self, owner_name):
        self.owner_name = owner_name

    def change_owner_surname(self, owner_surname):
        self.owner_surname = owner_surname

    def change_currency(self, currency):
        self.currency = currency
        self.balance *= EXCHANGE_RATES.get(currency)

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def transfer_money(self, amount):
        pass


class CreditCard(RegisterCardAccount):
    def __init__(
        self,
        account_nbr,
        owner_name,
        owner_surname,
        balance=0,
        currency="EUR",
        credit_limit=0,
        interest_rate=0,
        due_date_day=1,
    ):
        super().__init__(account_nbr, owner_name, owner_surname, balance, currency)
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
        self.due_date_day = due_date_day

    def change_credit_limit(self, credit_limit):
        self.credit_limit = credit_limit

    def change_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def change_due_date_day(self, due_date_day):
        self.due_date_day = due_date_day

    def __repr__(self):
        next_month = calendar.nextmonth(
            year=date.today().year, month=date.today().month
        )
        next_month = calendar.month_name[next_month[1]]
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency}\n"
            f"Credit limit: {self.credit_limit} {self.currency}\n"
            f"Interest rate: {self.interest_rate} %\n"
            f"Interest calculation starts from: {next_month} {self.due_date_day}"
        )


class DebitCard(RegisterCardAccount):
    def __repr__(self):
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency}"
        )

