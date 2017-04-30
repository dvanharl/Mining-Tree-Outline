import os , os.path
import sqlite3
import csv

# 
# Make the movie hash table
#
# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
# datadir = os.path.abspath(os.path.join(pardir , "data/"))
datadir = pardir.replace("/scripts" , "/data")

conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

movie_hash = {}
movie_id = 0

try:
	cur.execute("ALTER TABLE all_data ADD COLUMN movie_id 'NUMERIC'  ")
except:
	pass



# Build the hash
for row in cur.execute('SELECT movie_title FROM all_data'):
	movie = u''.join((row[0])).encode('utf8')
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

#
# Create the table and save the id
#
# Get the path for the database
conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

cur.execute("CREATE TABLE movie_id (movie_title TEXT, movie_id NUMERIC)")
with open(datadir + "/movie_hash.csv") as moviecsv:
	linereader = csv.reader(moviecsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split("~")
		movie = split_line[0]
		movie_id = split_line[1]
		cur.execute("INSERT INTO movie_id VALUES (?,?)" , (movie.decode("utf8") , movie_id))
conn.commit()

#
# Update the values
#

# Get the path for the database
conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

# Get the director relationships
with open(datadir + "/movie_hash.csv") as dircsv:
	linereader = csv.reader(dircsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split("~")
		movie = split_line[0]
		movie_id = split_line[1]
		cur.execute("UPDATE all_data SET movie_id = ? WHERE movie_title= ?" , (movie_id , movie.decode("utf8")))

conn.commit()
