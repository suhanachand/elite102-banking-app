import banking

print("Running tests...")

banking.create_account("Test User", 100)
banking.deposit(1, 50)
banking.withdraw(1, 30)
banking.check_balance(1)

print("Tests complete")
