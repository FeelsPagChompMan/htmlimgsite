from flask import Blueprint, render_template
from random import *

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Jonathan")
                           #, age=random.randint(1,2,3,4,5,6,7,8,9))
                           
@views.route("/yourname=<username>")
def profile(username):
    return render_template("index.html", name=username)

@views.route("/testing")
def test():
    return render_template("index.html")
