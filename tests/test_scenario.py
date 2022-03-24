from src.persons import Person, BankCustomer, BankEmployee
from src.card_accounts import CardAccount


def scenario1():
    bank_customer = BankCustomer()
    bank_employee = BankEmployee()
    
    credit_account = bank_employee.create_credit_account(bank_customer)
    credit_card = bank_employee.create_credit_card(bank_customer)
    bank_customer.add_money_to_account(credit_account)
