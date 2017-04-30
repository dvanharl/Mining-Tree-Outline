import os , os.path
import sqlite3
import csv

#
# Creates the ids and their associations
#

# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
# datadir = os.path.abspath(os.path.join(pardir , "data/"))
datadir = pardir.replace("/scripts" , "/data")


conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

dir_hash = {}
dir_id = 0

try:
	cur.execute("ALTER TABLE all_data ADD COLUMN director_id 'NUMERIC'")
except:
	pass




# Build the hash
for row in cur.execute('SELECT * FROM all_data'):
	director = u''.join((row[1])).encode('utf8').strip()
	try: 
		dir_hash[director]
	except KeyError:	
		dir_hash[director] = dir_id
		dir_id += 1

# Save it to the csv file		
with open(datadir + "/dir_hash.csv" , "w") as dir_file:
	string = ""
	for director , dir_id in dir_hash.items():
		string += director+":"
		string += str(dir_id)
		string += "\n"

	dir_file.write(string)
#
# Creates the table and saves it
#
conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

cur.execute("CREATE TABLE director_id (director_name TEXT, director_id NUMERIC)")

with open(datadir + "/dir_hash.csv") as dircsv:
	linereader = csv.reader(dircsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split(":")
		director = split_line[0]
		dir_id = split_line[1]
		cur.execute("INSERT INTO director_id VALUES (?,?)" , (director.decode("utf8") , str(dir_id)))

conn.commit()

#
# Updates the director values
#
conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

# Get the director relationships
with open(datadir + "/dir_hash.csv") as dircsv:
	linereader = csv.reader(dircsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split(":")
		director = split_line[0]
		dir_id = split_line[1]
		cur.execute("UPDATE all_data SET director_id = ? WHERE director_name = ?" , (dir_id, director.decode("utf8")))

conn.commit()
