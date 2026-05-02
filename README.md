# elite102-banking-app

banking system
description

this is a simple banking system built using python and sqlite. it allows users to create accounts and perform basic banking operations like deposits, withdrawals, transfers, and checking balances.

features
create a new bank account with a starting deposit
deposit money into an account
withdraw money if there are enough funds
transfer money between accounts
check account balance
view all accounts in the database
how it works

the program connects to a sqlite database using a helper function in database.py. each function opens a connection, runs the needed sql command, and then closes the connection.

for transfers, the program checks that both accounts exist and that the sender has enough money before completing the transaction.

setup
make sure python is installed
run or import the project files
ensure the database has an accounts table with id, name, and balance

example table setup:

create table accounts (
    id integer primary key autoincrement,
    name text not null,
    balance real default 0
);
how to use

you can import the functions and call them directly:

from banking import create_account, deposit, withdraw, transfer, check_balance

create_account("john", 1000)
deposit(1, 200)
withdraw(1, 100)
check_balance(1)
notes

this project is for learning purposes
there is no login or security system
each function connects to the database separately
