class InsufficientFundsError(ValueError):
    pass


class AgeError(ValueError):
    pass


class CurrencyError(ValueError):
    pass


class AccountExistenceError(KeyError):
    pass
