import os , os.path
import sqlite3
import csv

# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
datadir = os.path.abspath(os.path.join(pardir , "data/"))

conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

cur.execute("CREATE TABLE movie_id (movie_title TEXT, movie_id NUMERIC)")
with open(datadir + "/movie_hash.csv") as moviecsv:
	linereader = csv.reader(moviecsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split("~")
		movie = split_line[0]
		movie_id = split_line[1]
		cur.execute("INSERT INTO movie_id VALUES (?,?)" , (movie.decode("utf8") , str(movie_id)))
conn.commit()
