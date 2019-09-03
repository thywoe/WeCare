from cs50 import SQL

from flask import Flask, redirect, render_template, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

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




