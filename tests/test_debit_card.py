import pytest
from src.card_accounts import DebitCard
from src.errors import InsufficientFundsError


@pytest.fixture
def debit_card():
    return DebitCard(
        account_nbr="000000001", currency_code="GBP", balance=100, status="ACTIVE"
    )


def test_init():
    debit_card = DebitCard(
        account_nbr="000000001", currency_code="GBP", balance=100, status="ACTIVE"
    )
    assert debit_card.account_nbr == "000000001"
    assert debit_card.currency_code == "GBP"
    assert debit_card.balance == 100
    assert debit_card.status == "ACTIVE"


def test_deposit_money(debit_card):
    debit_card.deposit_money(15)
    assert debit_card.balance == 115


def test_withdraw_money_success(debit_card):
    debit_card.withdraw_money(20)
    assert debit_card.balance == 80


def test_withdraw_money_insufficient_funds_error(debit_card):
    with pytest.raises(Exception) as e:
        debit_card.withdraw_money(101)
        assert InsufficientFundsError == e


def test_repr(debit_card):
    assert (
        repr(debit_card)
        == "Account number: 000000001\nBalance: 100 GBP\nStatus: ACTIVE"
    )
