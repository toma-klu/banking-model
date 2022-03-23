from src.config import EXCHANGE_RATES


class Currency:
    def __init__(self, currency: str) -> None:
        self.currency = currency
        self.exchange_rate = EXCHANGE_RATES.get((currency, currency), 1)

    def change_currency(self, currency: str) -> None:
        self.exchange_rate = EXCHANGE_RATES.get((self.currency, currency), 1)
        self.currency = currency


class InsufficientFunds(Exception):
    def __init__(self) -> None:
        self.message = "Insufficient funds"
