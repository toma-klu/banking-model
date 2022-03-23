import pytest
from src.persons import Person


@pytest.fixture
def person():
    return Person(name="Jonas", surname="Jonaitis")


def test_init(person):
    assert person.name == "Jonas"
    assert person.surname == "Jonaitis"


def test_change_name(person):
    person.change_name("Jonukas")
    assert person.name == "Jonukas"


def test_change_surname(person):
    person.change_surname("Petraitis")
    assert person.surname == "Petraitis"
