from baking_model import CreditCard
import pytest


@pytest.fixture
def credit_card():
    return CreditCard(
        account_nbr="LT000000001",
        owner_name="Jonas",
        owner_surname="Jonaitis",
        credit_limit=1000,
    )

def test_init():
    credit_card = CreditCard(
        account_nbr="LT000000001",
        owner_name="Jonas",
        owner_surname="Jonaitis",
        credit_limit=1000,
    )
    assert credit_card.account_nbr == "LT000000001"
    assert credit_card.owner_name == "Jonas"
    assert credit_card.owner_surname == "Jonaitis"
    assert credit_card.credit_limit == 1000


def test_change_owner_name(credit_card):
    credit_card.change_owner_name("Jonukas")
    assert credit_card.owner_name == "Jonukas"
