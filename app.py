import os
import datetime
import pytz
import sys
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

def username():
        id  = session["user_id"]
        username = db.execute("SELECT username FROM users WHERE id = ?", id)
        if username is None:
            return None
        else:
            return username[0]["username"]

def transaction_time():
    time = datetime.datetime.now(pytz.timezone("US/Eastern"))
    return time

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    #order details and shares of each bought companies, total cash
    portfolio = db.execute("SELECT symbols, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbols", username())
    data_list = []
    stock_price = 0.00
    for items in portfolio:
            look_up = lookup(items["symbols"])
            total = look_up["price"] * items["total_shares"]
            stock_price = stock_price + total
            data_list.append(look_up)
    cash = db.execute("SELECT cash FROM users WHERE username = ?", username())
    total_amt = stock_price + cash[0]["cash"]
    #price to be added
    return render_template("index.html", portfolio = portfolio, data_list = data_list, cash = cash[0]["cash"], total = total_amt)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        #getting neccessary data at once
        try:
            name = request.form.get("symbol")
            share = int(request.form.get("shares"))
        except:
            return apology("invalid value ")

        if name is None or share is None:
            return apology("Invalid ")

        data = lookup(name)

        if data is None:
            return apology("data[symbol]")

        available_cash = db.execute("SELECT cash FROM users WHERE username = ? ", username())

        if available_cash is None:
            return apology("no cash")
        #checking for possible errors

        if share <= 0:
            return apology("INVALID Symbol")
        if share * data["price"] > available_cash[0]["cash"]:
            return apology("bhikhaari sala")
        if not username == None:
             #store in sqlite table
            db.execute("INSERT INTO transactions (user_id, transaction_type, symbols, shares, price, transaction_time) VALUES (?, ?, ?, ?, ?, ?)", username(), 'buy', data["name"], share, data["price"], transaction_time())

            update_cash  = (available_cash[0]["cash"] - (share * data["price"]))
            db.execute("UPDATE users SET cash = ? where username = ?", update_cash, username())

            #redirect "TO HOMEPAGE
            return redirect("/")
        else:
            return render_template("login.html")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():

    """Show history of transactions"""
    data = db.execute("SELECT symbols, shares, price, transaction_time FROM transactions WHERE user_id = ? ORDER BY transaction_time DESC", username())

    return render_template("history.html", data = data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
       name = request.form.get("symbol")
       data = lookup(name)
       if name is None:
           return apology("invalid")
       if data is None:
           return apology("invalid")
       return render_template("quoted.html", Name = data["name"], Symbol = data["symbol"] , Price = data["price"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        check_usr = db.execute("SELECT username FROM users GROUP BY username")

        if username is None or not  len(username) > 1 or not len(password) > 1:
            return apology("Username/ Password Required!")
        if not password == confirmation:
            return apology("Password donot match")

        for users in check_usr:
            if users["username"] == username:
                return apology("username not available")

        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        try:
            sell_shares = int(request.form.get("shares"))
        except:
            return apology("invalid value")
        transaction_type = "sell"

    #for available balance
        sShares = db.execute("SELECT SUM(shares) AS sumsShares FROM transactions where user_id = ? AND symbols = ? AND transaction_type = 'sell'", username(), symbol)
        bShares = db.execute("SELECT SUM(shares) AS sumsShares FROM transactions where user_id = ? AND symbols = ? AND transaction_type = 'buy'", username(), symbol)
        look_up = lookup(symbol)
        sell_price = look_up["price"]
        if sShares[0]["sumsShares"] == None:
            available_shares = bShares[0]["sumsShares"]
        else:
            available_shares = bShares[0]["sumsShares"] - sShares[0]["sumsShares"]

        tTime = transaction_time()
    #error handling
        if sell_shares > available_shares:
            return apology("You don't have that much of shares")
        if symbol == None:
            return apology("Please choose a share symbol")
        if sell_shares <= 0:
            return apology("Please choose valid number of shares")

    #entering the selled share in db
        db.execute("UPDATE users SET cash = cash + ? WHERE username = ?", sell_price * sell_shares, username())
        db.execute("INSERT INTO transactions (user_id, transaction_type, symbols, shares, price, transaction_time) VALUES (?, ?, ?, ?, ?, ?)", username(), transaction_type, symbol, -sell_shares, sell_price, transaction_time())
        return redirect("/")

    else:
        db_symbols = db.execute("SELECT symbols FROM transactions where user_id = ? GROUP BY symbols", username())
        return render_template("sell.html", db_symbols = db_symbols)
