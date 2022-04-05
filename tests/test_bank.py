from src.banks import Bank


def test_init():
    bank = Bank(name="TomaBank")
    assert bank.name == "TomaBank"
    assert bank.account_nbr == "000000000"
    assert bank.account_creation_requests == []
    assert bank.account_shutdown_requests == []
    assert bank.currency_exchange_requests == []
