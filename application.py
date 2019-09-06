import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQL("sqlite:///wecare.db")



@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user = db.execute("SELECT location FROM users WHERE id=:userid", userid=session["user_id"])
    location = user[0]["location"]
    rows = db.execute("SELECT * FROM hospital WHERE location=:location",location=location)

    return render_template("index.html",rows=rows)






@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("email"):
            return apology("must provide username",403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE email = :email", email = request.form.get("email"))

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]
        session["admin"] = rows[0]["isAdmin"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():
    

    """Register user"""
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        num = request.form.get("number")
        number = int(num)
        user_type = request.form.get("user_type")
        email = request.form.get("email")
        location = request.form.get("location")


        if not username:
            return apology("username is empty",400)
        elif not password:
            return apology("password is empty",400)
        elif not confirm:
            return apology("confirm password is empty",400)
        elif password != confirm:
            return apology("password doesn't match",400)
        elif not num:
            return apology("number field is empty",400)
        elif not email:
            return apology("email field is empty",400)
        elif not user_type:
            return apology("user field is not checked",400)
        elif not location:
            return apology("location field is empty",400)
        hash_password = generate_password_hash(password)

        if user_type == "user":
            row = db.execute("INSERT INTO users(username,password,email,phone_no,location) VALUES(:username,:password,:email,:phone_no,:location)",
             username=username, password=hash_password, email=email, phone_no=number,location=location)
            return redirect("/")
        elif user_type == "hospital":
            row = db.execute("INSERT INTO users(username,password,email,phone_no,location,isAdmin) VALUES(:username,:password,:email,:phone_no,:location,:admin)",
             username=username, password=hash_password,email=email, phone_no=number,location=location,admin=1)
            return redirect("/hospital")
    else:
        return render_template("register.html")

@app.route("/hospital", methods=["GET", "POST"])
@login_required
def hospital():
    if request.method == "POST":
        name = request.form.get("hospital_name")
        address = request.form.get("hospital_add")
        am = request.form.get("apt_times_am")
        contact = request.form.get("hospital_pwd")
        pm = request.form.get("apt_times_pm")
        email = request.form.get("email")
        location = request.form.get("location")
        max_apt = int(request.form.get("max_apt"))

        if not name:
            return apology("Hospital name is empty",400)
        elif not address:
            return apology("Hospital address is empty",400)
        elif not am:
            return apology("AM appointment time is empty",400)
        elif not contact:
            return apology("Hospital contact is empty",400)
        elif not pm:
            return apology("PM appointment time is empty",400)
        elif not email:
            return apology("Hospital email is empty",400)
        elif not location:
            return apology("Hospital location is empty",400)
        elif not max_apt:
            return apology("Number of appointment is empty",400)

        row = db.execute("INSERT INTO users(name,address,email,contact,location,am,pm,max_apt) VALUES(:name,:address,:email,:contact,:location,:am,:pm,:max_apt)",
             name=name, address=address,email=email, contact=contact,location=location,am=am,pm=pm,max_apt=max_apt)
        return redirect("/dashboard")

    else:
        return render_template("hospital-form.html")

    





