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

# Get the director relationships
with open(datadir + "/movie_hash.csv") as dircsv:
	linereader = csv.reader(dircsv , delimiter = "\n")
	for line in linereader:
		# print line[0].split("~")[0].replace("\xc2\xa0", "").decode("utf8")
		split_line = line[0].split("~")
		movie = split_line[0]
		# for letter in movie:
		#	print letter
		movie_id = split_line[1]
		# if movie == "Daredevil ":
	#	raw_input(movie)
		# raw_input(movie_id)
		cur.execute("UPDATE all_data SET movie_title = ? WHERE movie_title = ?" , (str(movie_id) , movie.decode("utf8")))

conn.commit()
