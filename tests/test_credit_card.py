import pytest
from src.card_accounts import CreditCard


@pytest.fixture
def credit_card():
    return CreditCard(
        account_nbr="LT000000001",
        personal_id_nbr="39201101213",
        name="Jonas",
        surname="Jonaitis",
        balance=100,
        credit_limit=1000,
        interest_rate=0.05,
    )


def test_init(credit_card):
    assert credit_card.account_nbr == "LT000000001"
    assert credit_card.personal_id_nbr == "39201101213"
    assert credit_card.name == "Jonas"
    assert credit_card.surname == "Jonaitis"
    assert credit_card.currency == "EUR"
    assert credit_card.balance == 100
    assert credit_card.status == "ACTIVE"
    assert credit_card.credit_limit == 1000
    assert credit_card.interest_rate == 0.05
    assert credit_card.due_date_day == 1


def test_change_credit_limit(credit_card):
    credit_card.change_credit_limit(500)
    assert credit_card.credit_limit == 500


def test_change_interest_rate(credit_card):
    credit_card.change_interest_rate(0.06)
    assert credit_card.interest_rate == 0.06


def change_due_date_day(credit_card):
    credit_card.change_due_date_day(2)
    assert credit_card.due_date_day == 2


def test_repr(credit_card):
    assert repr(credit_card) == (
        f"Account number: LT000000001\n"
        f"Balance: 100 EUR\n"
        f"Credit limit: 1000 EUR\n"
        f"Interest rate: 0.05 %\n"
        f"Interest calculation starts from: April 1"
    )
