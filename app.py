# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request
import requests
import schedule
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '''<form method="post">
    EVAL<textarea  type="text" name="res"></textarea><br>
    CRON<input  type="text" name="cron"><br>
    <input type="submit">
    </form>'''


@app.route('/', methods=['POST'])
def eval():
    dinge = request.form['res']
    print("Evaluating", dinge)
    ev = safe_eval(dinge)
    print("Evaluated", ev)
    ev["cron"] = request.form["cron"]
    return ev or "KAPUTT"


def safe_eval(to_eval):
    # Use a breakpoint in the code line below to debug your script.
    scope = {"open": None, "file": None, "csv": None, "json": None, "sqlite3": None, "sys": None, "exit": None,
             "scope": None, "eval": None, "exec": None, "to_eval": None, "os": None}
    loc = {}
    scope = {"print": print, "requests": requests}
    exec(to_eval, scope, loc)
    return loc
