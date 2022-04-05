import pytest
from src.customers import Customer


@pytest.fixture
def customer():
    return Customer(
        personal_id_nbr="123456789", name="Jonas", surname="Jonaitis", age=22
    )


def test_init():
    customer = Customer(
        personal_id_nbr="123456789", name="Jonas", surname="Jonaitis", age=22
    )
    assert customer.personal_id_nbr == "123456789"
    assert customer.name == "Jonas"
    assert customer.surname == "Jonaitis"
    assert customer.age == 22
    assert customer.accounts == {}


def test_change_name(customer):
    customer.change_name("Jonukas")
    assert customer.name == "Jonukas"


def test_change_surname(customer):
    customer.change_surname("Petraitis")
    assert customer.surname == "Petraitis"


def test_repr(customer):
    assert repr(customer) == (
        "PERSONAL INFORMATION:\n\n"
        "Personal ID number: 123456789\n"
        "Name: Jonas\n"
        "Surname: Jonaitis\n"
        "Age: 22\n\n"
        "ACCOUNT INFORMATION:\n\n"
        "No accounts"
    )
