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

dir_hash = {}
dir_id = 0

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
