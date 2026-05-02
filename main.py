from database import create_tables
import banking

create_tables()

print("=== Welcome to Banking System ===")

while True:
    print("\n1. Create Account")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        deposit = float(input("Initial deposit: "))
        banking.create_account(name, deposit)

    elif choice == "5":
        break
