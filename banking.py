from database import connect


def create_account(name, deposit):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, deposit)
    )

    conn.commit()

    account_id = cursor.lastrowid

    conn.close()

    print("Account created!")
    print("Account ID:", account_id)

    return account_id


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

    if not result:
        print("Account not found")
        conn.close()
        return

    if result[0] >= amount:
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, account_id)
        )
        conn.commit()
        print("Withdrawal successful")
    else:
        print("Insufficient funds")

    conn.close()


def check_balance(account_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return None


def list_accounts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, balance FROM accounts")
    accounts = cursor.fetchall()

    conn.close()

    print("ID | Name | Balance")
    print("--------------------")

    for acc in accounts:
        print(f"{acc[0]} | {acc[1]} | {acc[2]}")


def transfer(from_id, to_id, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (from_id,))
    sender = cursor.fetchone()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (to_id,))
    receiver = cursor.fetchone()

    if not sender:
        print("Sender account not found")
        conn.close()
        return

    if not receiver:
        print("Receiver account not found")
        conn.close()
        return

    if sender[0] < amount:
        print("Insufficient funds")
        conn.close()
        return

    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",
        (amount, from_id)
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, to_id)
    )

    conn.commit()
    conn.close()

    print("Transfer successful")

def show_accounts_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, balance FROM accounts")
    accounts = cursor.fetchall()

    conn.close()

    print("\ncurrent accounts")
    print("id | name | balance")
    print("--------------------")

    for acc in accounts:
        print(f"{acc[0]} | {acc[1]} | {acc[2]}")
