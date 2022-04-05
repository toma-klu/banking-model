from src.customers import Customer


class RequestDebitCardAccountCreation:
    def __init__(self, customer: Customer, currency_code: str = "EUR") -> None:
        self.customer = customer
        self.currency_code = currency_code


class RequestCreditCardAccountCreation:
    def __init__(
        self,
        customer: Customer,
        credit_limit: float,
        due_date_day: int,
        currency_code: str = "EUR",
    ) -> None:
        self.customer = customer
        self.credit_limit = credit_limit
        self.due_date_day = due_date_day
        self.currency_code = currency_code


class RequestAccountShutdown:
    def __init__(self, customer: Customer, account_nbr: str) -> None:
        self.customer = customer
        self.account_nbr = account_nbr


class RequestCurrencyExchange:
    def __init__(
        self, customer: Customer, account_nbr: str, currency_code: str
    ) -> None:
        self.customer = customer
        self.account_nbr = account_nbr
        self.currency_code = currency_code
