import calendar
from datetime import date
from src.persons import BankCustomer
from src.helpers import InsufficientFunds, Currency


class CardAccount(BankCustomer, Currency):
    def __init__(
        self,
        account_nbr: str,
        personal_id_nbr: str,
        name: str,
        surname: str,
        currency: str = "EUR",
        balance: float = 0,
        status: str = "ACTIVE",
    ) -> None:
        BankCustomer.__init__(self, personal_id_nbr, name, surname)
        Currency.__init__(self, currency)
        self.account_nbr = account_nbr
        self.balance = balance
        self.status = status

    def change_currency(self, currency: str) -> None:
        Currency.change_currency(self, currency)
        self.balance *= self.exchange_rate

    def deposit_money(self, amount: float) -> None:
        self.balance += amount

    def withdraw_money(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise InsufficientFunds()

    # Finalize this method
    def transfer_money(self, amount: float, account_nbr: str) -> None:
        if amount <= self.balance:
            pass
        else:
            raise InsufficientFunds()

    def __repr__(self) -> str:
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency}"
        )


class CreditCard(CardAccount):
    def __init__(
        self,
        account_nbr: str,
        personal_id_nbr: str,
        name: str,
        surname: str,
        currency: str = "EUR",
        balance: float = 0,
        status: str = "ACTIVE",
        credit_limit: float = 0,
        interest_rate: float = 0,
        due_date_day: int = 1,
    ) -> None:
        CardAccount.__init__(
            self,
            account_nbr,
            personal_id_nbr,
            name,
            surname,
            currency,
            balance,
            status,
        )
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
        self.due_date_day = due_date_day

    def change_credit_limit(self, credit_limit: float) -> None:
        self.credit_limit = credit_limit

    def change_interest_rate(self, interest_rate: float) -> None:
        self.interest_rate = interest_rate

    def change_due_date_day(self, due_date_day: int) -> None:
        self.due_date_day = due_date_day

    def __repr__(self) -> str:
        next_month = calendar.nextmonth(  # type: ignore
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


# This class is exactly the same as general CardAccount class, but it is
# created to better describe what kind of account is created
class DebitCard(CardAccount):
    pass
