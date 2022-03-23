import pytest
from src.card_accounts import CardAccount
from src.helpers import InsufficientFunds


@pytest.fixture
def card_account():
    return CardAccount(
        account_nbr="LT000000001",
        personal_id_nbr="39201101213",
        name="Jonas",
        surname="Jonaitis",
        currency="GBP",
        balance=100,
    )


def test_init(card_account):
    assert card_account.account_nbr == "LT000000001"
    assert card_account.personal_id_nbr == "39201101213"
    assert card_account.name == "Jonas"
    assert card_account.surname == "Jonaitis"
    assert card_account.currency == "GBP"
    assert card_account.balance == 100
    assert card_account.status == "ACTIVE"


def test_change_currency(card_account):
    card_account.change_currency("USD")
    assert card_account.balance == 132.12


def test_deposit_money(card_account):
    card_account.deposit_money(15)
    assert card_account.balance == 115


def test_withdraw_money_1(card_account):
    card_account.withdraw_money(20)
    assert card_account.balance == 80


def test_withdraw_money_2(card_account):
    with pytest.raises(Exception) as e:
        card_account.withdraw_money(101)
        assert InsufficientFunds == e


def test_transfer_money(card_account):
    pass


def test_repr(card_account):
    assert repr(card_account) == f"Account number: LT000000001\n" f"Balance: 100 GBP"
