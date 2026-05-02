
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
