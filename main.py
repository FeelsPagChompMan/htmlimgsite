from flask import Blueprint, render_template

main = Blueprint(__name__, "home")

@main.route("/")
def home():
    return render_template("home.html")