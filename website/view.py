from flask import Blueprint, render_template, request, redirect, url_for

from website.user_login import loginuser, newUser


#SQL for movie information

import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database="skymovie_christmas"
    )


my_cursor = db.cursor()
query = ("SELECT film_title, film_synopsis, title_image, film_year, film_cert, sky_store  FROM movies order by rand() limit 6")
my_cursor.execute(query)

movies = my_cursor.fetchall()

# my_cursor = db.cursor()
# query = ("SELECT film_synopsis FROM movies limit 3")
# my_cursor.execute(query)
# movie_synopsis=my_cursor.fetchall()
    # for m in my_cursor:
    #print (movies)

#
views = Blueprint('views', __name__)

@views.route('/')
def Home():
    return render_template("home.html", title='Home', movies=movies)


@views.route('/VIP/<name>', methods=['GET'])
def loggedIn(name):
    return render_template("VIP.html", name=name)

@views.route('VIP')
def VIP():
    return render_template("VIP.html", title='Sky VIP')

@views.route('login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            username = request.form['username']
            password = request.form['password']

            welcome = loginuser(username, password)

            return redirect(url_for('views.loggedIn', name=welcome))
    return render_template('login.html', error=error, title='Login')



@views.route('quiz')
def Quiz():
    return render_template("CharacterQuiz.html", title='Quiz')


@views.route('register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '' or request.form['con_password'] == '' or request.form['email'] == '':
            error = 'Invalid Credentials. Please try again.'
        else:
            userName = request.form['username']
            password = request.form['password']
            passwordConfirm = request.form['con_password']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            reg_name = newUser(firstname, lastname, email, userName, password, passwordConfirm)
        return redirect(url_for("views.success", title='Success', name=reg_name))
    return render_template("register.html", error=error, title='Register')

@views.route('/success/<name>', methods=['GET'])
def success(name):
        # if name == 'Username%20already%20exists!!!':
        #     outcome = 'Username already exists!'
        # else:
        #     pass

    return render_template("success.html", name=name)