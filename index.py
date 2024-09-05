from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(["jpg","jpeg"])


@app.route("/")
def hello_world():
    return render_template("activities.html",  text = "Hello, World!")