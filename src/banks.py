from typing import Union
from src.config import EXCHANGE_RATES
from src.requests import (
    RequestDebitCardAccountCreation,
    RequestCreditCardAccountCreation,
    RequestAccountShutdown,
    RequestCurrencyExchange,
)
from src.card_accounts import CreditCard, DebitCard
from src.errors import AgeError, CurrencyError, AccountExistenceError


class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        # Initial account number
        self.account_nbr = "000000000"
        self.account_creation_requests: list = []
        self.account_shutdown_requests: list = []
        self.currency_exchange_requests: list = []

    def add_account_creation_request(
        self,
        request: Union[
            RequestDebitCardAccountCreation, RequestCreditCardAccountCreation
        ],
    ) -> None:
        self.account_creation_requests.append(request)

    def add_account_shutdown_request(self, request: RequestAccountShutdown) -> None:
        self.account_shutdown_requests.append(request)

    def add_currency_exchange_request(self, request: RequestCurrencyExchange) -> None:
        self.currency_exchange_requests.append(request)

    def review_account_creation_requests(self) -> None:
        for request in self.account_creation_requests:
            self.account_creation_requests.remove(request)
            if isinstance(request, RequestDebitCardAccountCreation):
                self.approve_debit_card_account_creation_request(request)
            else:
                self.approve_credit_card_account_creation_request(request)

    def review_account_shutdown_requests(self) -> None:
        for request in self.account_shutdown_requests:
            self.account_shutdown_requests.remove(request)
            self.approve_account_shutdown_request(request)

    def review_currency_exchange_requests(self) -> None:
        for request in self.currency_exchange_requests:
            self.currency_exchange_requests.remove(request)
            self.approve_currency_exchange_request(request)

    def approve_debit_card_account_creation_request(
        self, request: RequestDebitCardAccountCreation
    ) -> None:
        self.account_nbr = str(int(self.account_nbr) + 1).zfill(len(self.account_nbr))
        request.customer.accounts[self.account_nbr] = DebitCard(
            account_nbr=self.account_nbr,
            currency_code=request.currency_code,
            balance=0,
            status="ACTIVE",
        )

    def approve_credit_card_account_creation_request(
        self, request: RequestCreditCardAccountCreation
    ) -> None:
        if request.customer.age > 20:
            self.account_nbr = str(int(self.account_nbr) + 1).zfill(
                len(self.account_nbr)
            )
            request.customer.accounts[self.account_nbr] = CreditCard(
                account_nbr=self.account_nbr,
                currency_code=request.currency_code,
                balance=request.credit_limit,
                status="ACTIVE",
                credit_limit=request.credit_limit,
                interest_rate=0.03 if request.customer.age > 30 else 0.05,
                due_date_day=request.due_date_day,
            )
        else:
            raise AgeError(
                "Customer should be at least 21 years old to register credit card account."
            )

    def approve_account_shutdown_request(self, request: RequestAccountShutdown) -> None:
        try:
            request.customer.accounts[request.account_nbr].status = "INACTIVE"
        except KeyError:
            raise AccountExistenceError(f"Account {self.account_nbr} does not exist.")

    def approve_currency_exchange_request(
        self, request: RequestCurrencyExchange
    ) -> None:
        try:
            exchange_rate = EXCHANGE_RATES.get(
                (
                    request.customer.accounts[request.account_nbr].currency_code,
                    request.currency_code,
                )
            )
            request.customer.accounts[request.account_nbr].balance = round(
                request.customer.accounts[request.account_nbr].balance * exchange_rate,
                2,
            )
            request.customer.accounts[
                request.account_nbr
            ].currency_code = request.currency_code
        except KeyError:
            raise CurrencyError("Bank does not support this currency.")

    def __repr__(self) -> str:
        return (
            f"Bank name: {self.name}\n"
            f"Number of account creation requests: {len(self.account_creation_requests)}\n"
            f"Number of account shutdown requests: {len(self.account_shutdown_requests)}\n"
            f"Number of currency exchange requests: {len(self.currency_exchange_requests)}"
        )
