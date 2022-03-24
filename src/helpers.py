from src.config import EXCHANGE_RATES


class Currency:
    def __init__(self, currency: str) -> None:
        self.currency = currency
        # This can be buggy because, exchange rates can change
        self.exchange_rate = EXCHANGE_RATES.get((currency, currency), 1)

    # This function does not change currency. Ji issaugo nauja exchange rate
    # Change currency turetu tiesiog pakeisti currency EUR > DOL
    # ARBA 100 EUR > 110 DOL????? This function does not do that
    def change_currency(self, currency: str) -> None:
        self.exchange_rate = EXCHANGE_RATES.get((self.currency, currency), 1)
        self.currency = currency


# Its a kind of ValueError?
# Inherit from ValueError
class InsufficientFunds(Exception):
    def __init__(self) -> None:
        self.message = "Insufficient funds"
