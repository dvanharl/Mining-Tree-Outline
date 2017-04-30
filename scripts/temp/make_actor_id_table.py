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

cur.execute("CREATE TABLE actor_id (actor_name TEXT, actor_id TEXT)")

with open(datadir + "/actor_hash.csv") as actorcsv:
	linereader = csv.reader(actorcsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split(":")
		actor = split_line[0]
		actor_id = split_line[1]
		cur.execute("INSERT INTO actor_id VALUES (?,?)" , (actor.decode("utf8") , str(actor_id)))

conn.commit()
