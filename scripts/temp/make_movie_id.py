import os , os.path
import sqlite3
import json

# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
datadir = os.path.abspath(os.path.join(pardir , "data/"))

conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

movie_hash = {}
movie_id = 0

# Build the hash
for row in cur.execute('SELECT movie_title FROM all_data'):
	movie = u''.join((row[0])).encode('utf8')
	#if "Daredevil" in row[0]:
	#	print row[0].strip()
	try: 
		movie_hash[movie]
	except KeyError:	
		movie_hash[movie] = movie_id
		movie_id += 1

# Save it to the csv file		
with open(datadir + "/movie_hash.csv" , "w") as movie_file:
	string = ""
	for movie, movie_id in movie_hash.items():
		string += movie+"~"
		string += str(movie_id)
		string += "\n"

	movie_file.write(string)
