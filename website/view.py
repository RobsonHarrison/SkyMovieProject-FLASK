from flask import Blueprint, render_template, request, redirect, url_for

from website.user_login import loginuser

#SQL for movie information
import mysql.connector

db = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database="skymovie_christmas"
)
my_cursor = db.cursor()
query = ("SELECT film_title FROM movies")
my_cursor.execute(query)
for movies in my_cursor:
    movie_title = tuple(my_cursor.fetchall())
    # movie_title = movie_title_input[0]
    # print(type(movie_title))
my_cursor = db.cursor()
query = ("SELECT film_synopsis FROM movies")
my_cursor.execute(query)
for movies in my_cursor:
    #print (movies)
    movie_synopsis=my_cursor.fetchall()

views = Blueprint('views', __name__)

@views.route('/')
def Home():
    return render_template("home.html", title='Home', movietitle=movie_title, moviesynopsis=movie_synopsis)


@views.route('/home/<name>', methods=['GET'])
def loggedIn(name):
    return render_template("home.html", name=name, movietitle=movie_title, moviesynopsis=movie_synopsis)

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
    return render_template('login.html', error=error)
    #return render_template("login.html")

@views.route('CharacterQuiz')
def characterquiz():
    input_values = []
    if request.method == 'POST':
        Q1 = request.form['Question1']
        input_values.append(Q1)
        Q2 = request.form['Question2']
        input_values.append(Q2)
        Q3 = request.form['Question3']
        input_values.append(Q3)

    return render_template('CharacterQuiz.html', show=input_values, list=input_values)
