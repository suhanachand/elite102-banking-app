from database import create_tables
import banking

create_tables()
print("Loading Banking System...")
print("=== Welcome to Banking System ===")

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        deposit = float(input("Initial deposit: "))
        banking.create_account(name, deposit)

    elif choice == "2":
        acc_id = int(input("Account ID: "))
        amount = float(input("Amount: "))
        banking.deposit(acc_id, amount)

    elif choice == "3":
        acc_id = int(input("Account ID: "))
        amount = float(input("Amount: "))
        banking.withdraw(acc_id, amount)

    elif choice == "4":
        acc_id = int(input("Account ID: "))
        banking.check_balance(acc_id)

    elif choice == "5":
        banking.list_accounts()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")