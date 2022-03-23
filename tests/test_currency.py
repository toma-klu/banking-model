import pytest
from src.helpers import Currency


@pytest.fixture
def currency():
    return Currency(currency="GBP")


def test_init(currency):
    assert currency.currency == "GBP"
    assert currency.exchange_rate == 1


def test_change_currency(currency):
    currency.change_currency("EUR")
    assert currency.currency == "EUR"
    assert currency.exchange_rate == 1.2007
