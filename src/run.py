from baking_model import CreditCard

credit_card_1 = CreditCard(
    account_nbr="LT000000001",
    owner_name="Jonas",
    owner_surname="Jonaitis",
    credit_limit=1000,
)

print(credit_card_1)

credit_card_1.change_owner_name("Jonukas")

