
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


def check_balance(account_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        print("Balance:", result[0])
    else:
        print("Account not found")

def list_accounts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()

    conn.close()

    for acc in accounts:
        print(acc)

def transfer(from_id, to_id, amount):
    conn = connect()
    cursor = conn.cursor()

    # check sender balance
    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
    sender = cursor.fetchone()

    if sender and sender[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))
        conn.commit()
        print("Transfer successful")
    else:
        print("Insufficient funds or invalid account")

    conn.close()
