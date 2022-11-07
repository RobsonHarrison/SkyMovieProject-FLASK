from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def Home():
    return render_template("home.html")

@views.route('VIP')
def VIP():
    return render_template("VIP.html")

@views.route('login')
def login():
    return render_template("login.html")