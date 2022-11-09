from flask import Blueprint, render_template, request, redirect, url_for

from website.user_login import loginuser



views = Blueprint('views', __name__)

@views.route('/')
def Home():
    return render_template("home.html")


@views.route('/home/<name>', methods=['GET'])
def loggedIn(name):

    return render_template("home.html", name=name)

@views.route('VIP')
def VIP():
    return render_template("VIP.html")

@views.route('login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            username = request.form['username']
            password = request.form['password']

            loginuser(username, password)
            return redirect(url_for('views.loggedIn', name=username))
    return render_template('login.html', error=error)
    #return render_template("login.html")

@views.route('CharacterQuiz')
def characterquiz():
    input_values = []
    if request.method == 'POST':
        Q1 = request.form['Question1']
        input_values.append(Q1)

    return render_template('CharacterQuiz.html')