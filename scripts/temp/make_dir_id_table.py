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

cur.execute("CREATE TABLE director_id (director_name TEXT, director_id TEXT)")

with open(datadir + "/dir_hash.csv") as dircsv:
	linereader = csv.reader(dircsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split(":")
		director = split_line[0]
		dir_id = split_line[1]
		cur.execute("INSERT INTO director_id VALUES (?,?)" , (director.decode("utf8") , str(dir_id)))

conn.commit()