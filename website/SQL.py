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
    #print (movies)
    # print(type)
    movietitle=movies
    tupletitle = tuple(movies)
    print(tupletitle)






