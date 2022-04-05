import calendar
from datetime import date
from src.errors import InsufficientFundsError


class CardAccount:
    def __init__(
        self, account_nbr: str, currency_code: str, balance: float, status: str
    ) -> None:
        self.account_nbr = account_nbr
        self.currency_code = currency_code
        self.balance = balance
        self.status = status

    def deposit_money(self, amount: float) -> None:
        self.balance += amount

    def withdraw_money(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise InsufficientFundsError(
                f"Withdrawal ({amount} {self.currency_code}) cannot be bigger "
                f"than balance ({self.balance} {self.currency_code})."
            )

    def __repr__(self) -> str:
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency_code}\n"
            f"Status: {self.status}"
        )


class CreditCard(CardAccount):
    def __init__(
        self,
        account_nbr: str,
        currency_code: str,
        balance: float,
        status: str,
        credit_limit: float,
        interest_rate: float,
        due_date_day: int,
    ) -> None:
        CardAccount.__init__(
            self,
            account_nbr,
            currency_code,
            balance,
            status,
        )
        self.credit_limit = credit_limit
        self.interest_rate = interest_rate
        self.due_date_day = due_date_day

    def change_due_date_day(self, due_date_day: int) -> None:
        self.due_date_day = due_date_day

    def __repr__(self) -> str:
        next_month = calendar.nextmonth(  # type: ignore
            year=date.today().year, month=date.today().month
        )
        next_month = calendar.month_name[next_month[1]]
        return (
            f"Account number: {self.account_nbr}\n"
            f"Balance: {self.balance} {self.currency_code}\n"
            f"Credit limit: {self.credit_limit} {self.currency_code}\n"
            f"Interest rate: {self.interest_rate} %\n"
            f"Interest calculation starts from: {next_month} {self.due_date_day}\n"
            f"Status: {self.status}"
        )


# This class is exactly the same as general CardAccount class, but it is
# created to better describe what kind of account is created
class DebitCard(CardAccount):
    pass
