import pytest
from src.card_accounts import CreditCard


@pytest.fixture
def credit_card():
    return CreditCard(
        account_nbr="000000001",
        currency_code="EUR",
        balance=100,
        status="ACTIVE",
        credit_limit=1000,
        interest_rate=0.05,
        due_date_day=2,
    )


def test_init():
    credit_card = CreditCard(
        account_nbr="000000001",
        currency_code="EUR",
        balance=100,
        status="ACTIVE",
        credit_limit=1000,
        interest_rate=0.05,
        due_date_day=2,
    )
    assert credit_card.account_nbr == "000000001"
    assert credit_card.currency_code == "EUR"
    assert credit_card.balance == 100
    assert credit_card.status == "ACTIVE"
    assert credit_card.credit_limit == 1000
    assert credit_card.interest_rate == 0.05
    assert credit_card.due_date_day == 2


def change_due_date_day(credit_card):
    credit_card.change_due_date_day(3)
    assert credit_card.due_date_day == 3


def test_repr(credit_card):
    assert repr(credit_card) == (
        "Account number: 000000001\n"
        "Balance: 100 EUR\n"
        "Credit limit: 1000 EUR\n"
        "Interest rate: 0.05 %\n"
        "Interest calculation starts from: May 2\n"
        "Status: ACTIVE"
    )
