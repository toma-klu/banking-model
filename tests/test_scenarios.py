import pytest
from src.banks import Bank
from src.requests import (
    RequestDebitCardAccountCreation,
    RequestCreditCardAccountCreation,
    RequestCurrencyExchange,
    RequestAccountShutdown,
)
from src.customers import Customer
from src.errors import InsufficientFundsError, AccountExistenceError, AgeError, CurrencyError


def test_scenario_1():
    bank = Bank(name="TomaBank")
    assert bank.name == "TomaBank"
    assert repr(bank) == (
        "Bank name: TomaBank\n"
        "Number of account creation requests: 0\n"
        "Number of account shutdown requests: 0\n"
        "Number of currency exchange requests: 0"
    )
    customer_1 = Customer(
        personal_id_nbr="123456789", name="Jonas", surname="Jonaitis", age=21
    )
    assert repr(customer_1) == (
        "PERSONAL INFORMATION:\n\n"
        "Personal ID number: 123456789\n"
        "Name: Jonas\n"
        "Surname: Jonaitis\n"
        "Age: 21\n\n"
        "ACCOUNT INFORMATION:\n\n"
        "No accounts"
    )
    customer_1.change_name("Petras")
    customer_1.change_surname("Petraitis")
    assert customer_1.name == "Petras"
    assert customer_1.surname == "Petraitis"
    customer_1_request_debit_card = RequestDebitCardAccountCreation(customer_1)
    bank.add_account_creation_request(customer_1_request_debit_card)
    assert repr(bank) == (
        f"Bank name: TomaBank\n"
        f"Number of account creation requests: 1\n"
        f"Number of account shutdown requests: 0\n"
        f"Number of currency exchange requests: 0"
    )
    bank.review_account_creation_requests()
    assert repr(customer_1) == (
        "PERSONAL INFORMATION:\n\n"
        "Personal ID number: 123456789\n"
        "Name: Petras\n"
        "Surname: Petraitis\n"
        "Age: 21\n\n"
        "ACCOUNT INFORMATION:\n\n"
        "Account number: 000000001\n"
        "Balance: 0 EUR\n"
        "Status: ACTIVE"
    )
    customer_1.accounts["000000001"].deposit_money(100)
    assert customer_1.accounts["000000001"].balance == 100
    customer_1.accounts["000000001"].withdraw_money(60)
    assert customer_1.accounts["000000001"].balance == 40
    with pytest.raises(Exception) as e:
        customer_1.account["000000001"].withdraw_money(60)
        assert InsufficientFundsError == e
    customer_1_request_currency_exchange_success = RequestCurrencyExchange(
        customer=customer_1, account_nbr="000000001", currency_code="USD"
    )
    bank.add_currency_exchange_request(customer_1_request_currency_exchange_success)
    assert repr(bank) == (
        f"Bank name: TomaBank\n"
        f"Number of account creation requests: 0\n"
        f"Number of account shutdown requests: 0\n"
        f"Number of currency exchange requests: 1"
    )
    bank.review_currency_exchange_requests()
    assert customer_1.accounts["000000001"].currency_code == "USD"
    assert customer_1.accounts["000000001"].balance == 44.02
    customer_1_request_currency_currency_error = RequestCurrencyExchange(
        customer=customer_1, account_nbr="000000001", currency_code="USDD"
    )
    bank.add_currency_exchange_request(customer_1_request_currency_currency_error)
    with pytest.raises(Exception) as e:
        bank.review_currency_exchange_requests()
        assert CurrencyError == e
    customer_1_request_credit_card = RequestCreditCardAccountCreation(
        customer=customer_1, credit_limit=1000, due_date_day=2, currency_code="GBP"
    )
    bank.add_account_creation_request(customer_1_request_credit_card)
    bank.review_account_creation_requests()
    assert repr(customer_1) == (
        "PERSONAL INFORMATION:\n\n"
        "Personal ID number: 123456789\n"
        "Name: Petras\n"
        "Surname: Petraitis\n"
        "Age: 21\n\n"
        "ACCOUNT INFORMATION:\n\n"
        "Account number: 000000001\n"
        "Balance: 44.02 USD\n"
        "Status: ACTIVE\n\n"
        "Account number: 000000002\n"
        "Balance: 1000 GBP\n"
        "Credit limit: 1000 GBP\n"
        "Interest rate: 0.05 %\n"
        "Interest calculation starts from: May 2\n"
        "Status: ACTIVE"
    )
    customer_1_request_account_shutdown_success = RequestAccountShutdown(
        customer=customer_1, account_nbr="000000002"
    )
    bank.add_account_shutdown_request(customer_1_request_account_shutdown_success)
    assert repr(bank) == (
        f"Bank name: TomaBank\n"
        f"Number of account creation requests: 0\n"
        f"Number of account shutdown requests: 1\n"
        f"Number of currency exchange requests: 0"
    )
    bank.review_account_shutdown_requests()
    assert repr(customer_1) == (
        "PERSONAL INFORMATION:\n\n"
        "Personal ID number: 123456789\n"
        "Name: Petras\n"
        "Surname: Petraitis\n"
        "Age: 21\n\n"
        "ACCOUNT INFORMATION:\n\n"
        "Account number: 000000001\n"
        "Balance: 44.02 USD\n"
        "Status: ACTIVE\n\n"
        "Account number: 000000002\n"
        "Balance: 1000 GBP\n"
        "Credit limit: 1000 GBP\n"
        "Interest rate: 0.05 %\n"
        "Interest calculation starts from: May 2\n"
        "Status: INACTIVE"
    )
    customer_1_request_account_shutdown_account_existence_error = (
        RequestAccountShutdown(customer=customer_1, account_nbr="000000003")
    )
    with pytest.raises(Exception) as e:
        bank.add_account_shutdown_request(
            customer_1_request_account_shutdown_account_existence_error
        )
        assert AccountExistenceError == e


def test_scenario_2():
    bank = Bank(name="TomaBank")
    customer_1 = Customer(
        personal_id_nbr="123456789", name="Jonas", surname="Jonaitis", age=20
    )
    customer_1_request_credit_card_age_error = RequestCreditCardAccountCreation(
        customer=customer_1, credit_limit=1000, due_date_day=2, currency_code="GBP"
    )
    bank.add_account_creation_request(customer_1_request_credit_card_age_error)
    with pytest.raises(Exception) as e:
        bank.review_account_creation_requests()
        assert AgeError == e

