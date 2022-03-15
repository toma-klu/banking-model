from baking_model import CreditCard
import pytest

def test_notsure():
    credit_card = CreditCard(
        account_nbr="LT000000001",
        owner_name="Jonas",
        owner_surname="Jonaitis",
        credit_limit=1000,
    )

    credit_card.deposit_money(1000)
    assert credit_card.balance == 1000

    credit_card.withdraw_money(800)
    assert credit_card.balance == 200

    # TODO, again, we should catch a custom error.
    with pytest.raises(Exception) as e:
        credit_card.withdraw_money(9999)