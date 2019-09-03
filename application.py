from cs50 import SQL

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

app = Flask(__name__)

#Ensure templates auto-reloads
app.config["TEMPLATES_AUTO_RELOADED"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "filesystem"
Session(app)

db = SQL("sqlite:///wecare.db")

@app.route("/login", methods=["GET", "POST"])
def login():
    # session.clear()

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
            row = db.execute("INSERT INTO users(username,password,email,phone_no,location) VALUES(:username,:password,:email,:phone_no,location)",
             username=username, password=hash_password, email=email, phone_no=number,location=location)
            return redirect("/")
        elif user_type == "hospital":
            row = db.execute("INSERT INTO users(username,password,email,phone_no,location,isAdmin) VALUES(:username,:password,:email,:phone_no,:location,:admin)",
             username=username, password=hash_password,email=email, phone_no=number,location=location,admin=1)
            return redirect("/hospital")
    else:
        return render_template("register.html")





