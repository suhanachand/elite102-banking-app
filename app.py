from flask import Flask, render_template, request
import banking
from database import create_tables, connect

app = Flask(__name__)
create_tables()

@app.route("/")
def home():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    conn.close()

    return render_template("index.html", accounts=accounts, message=None)


@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    deposit = float(request.form["deposit"])

    acc_id = banking.create_account(name, deposit)

    return home_message(f"Account created! Your account ID is {acc_id}")


@app.route("/deposit", methods=["POST"])
def deposit():
    acc_id = int(request.form["id"])
    amount = float(request.form["amount"])
    banking.deposit(acc_id, amount)

    return home_message("Deposit successful!")


@app.route("/withdraw", methods=["POST"])
def withdraw():
    acc_id = int(request.form["id"])
    amount = float(request.form["amount"])
    banking.withdraw(acc_id, amount)

    return home_message("Withdraw processed!")


@app.route("/balance", methods=["POST"])
def balance():
    acc_id = int(request.form["id"])
    bal = banking.check_balance(acc_id)

    if bal is None:
        msg = "Account not found"
    else:
        msg = f"Current balance: {bal}"

    return home_message(msg)


def home_message(msg):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    conn.close()

    return render_template("index.html", accounts=accounts, message=msg)


@app.route("/transfer", methods=["POST"])
def transfer_route():
    from_id = int(request.form["from_id"])
    to_id = int(request.form["to_id"])
    amount = float(request.form["amount"])

    banking.transfer(from_id, to_id, amount)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
