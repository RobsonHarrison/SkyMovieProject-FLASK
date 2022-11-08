from flask import Blueprint, render_template

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

@views.route('VIP')
def VIP():
    return render_template("VIP.html", title='Sky VIP')

@views.route('login')
def login():
    return render_template("login.html", title='My Account')