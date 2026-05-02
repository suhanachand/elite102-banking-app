from flask import Flask, render_template, request, redirect
import banking
from database import create_tables

app = Flask(__name__)
create_tables()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    deposit = float(request.form["deposit"])
    banking.create_account(name, deposit)
    return redirect("/")

@app.route("/deposit", methods=["POST"])
def deposit():
    acc_id = int(request.form["id"])
    amount = float(request.form["amount"])
    banking.deposit(acc_id, amount)
    return redirect("/")

@app.route("/withdraw", methods=["POST"])
def withdraw():
    acc_id = int(request.form["id"])
    amount = float(request.form["amount"])
    banking.withdraw(acc_id, amount)
    return redirect("/")

@app.route("/balance", methods=["POST"])
def balance():
    acc_id = int(request.form["id"])
    banking.check_balance(acc_id)
    return redirect("/")

@app.route("/transfer", methods=["POST"])
def transfer_route():
    from_id = int(request.form["from_id"])
    to_id = int(request.form["to_id"])
    amount = float(request.form["amount"])

    banking.transfer(from_id, to_id, amount)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
