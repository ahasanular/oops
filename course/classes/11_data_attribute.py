class BankAccount:
    account_type = "Credit"
    interest = 1.2

acc_1 = BankAccount()
acc_2 = BankAccount()


print(acc_1.__dict__)

print(acc_1.account_type, acc_2.account_type)
print(acc_1.interest, acc_2.interest)

acc_1.account_type = "Savings"
# setattr(acc_1, "created", "1 year")
BankAccount.created = "1 year"



print(acc_1.account_type, acc_2.account_type)
print(acc_1.interest, acc_2.interest)
print(BankAccount.interest, BankAccount.account_type)

"""
    content:
        instances attr change not affect Class attr
        class attr change also not affects instance attr but can access from INSTANCES
        it searches class after instace for a attr
        search sequence === instance >> Class. [if no attr found return AttributeError]

    summary:
        CLASSES and INSTANCES has their onw STATE. They maintain their own dictionary in methode named "__dict__".
"""