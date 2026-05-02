
from database import connect

def create_account(name, deposit):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, deposit)
    )

    conn.commit()
    conn.close()

    print("Account created!")


def deposit(account_id, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, account_id)
    )

    conn.commit()
    conn.close()

    print("Deposit successful")

def withdraw(account_id, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
    result = cursor.fetchone()

    if result and result[0] >= amount:
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, account_id)
        )
        print("Withdrawal successful")
    else:
        print("Insufficient funds")

    conn.commit()
    conn.close()
