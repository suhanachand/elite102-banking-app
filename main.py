from database import create_tables
import banking
import os

create_tables()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear_screen()

    print("BANKING SYSTEM")

    # ALWAYS SHOW TABLE FIRST
    banking.show_accounts_table()

    print("\nmenu")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Exit")

    choice = input("\nEnter choice: ")

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
        input("press enter to continue")

    elif choice == "5":
        from_id = int(input("From Account ID: "))
        to_id = int(input("To Account ID: "))
        amount = float(input("Amount: "))
        banking.transfer(from_id, to_id, amount)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

    input("\npress enter to continue...")
