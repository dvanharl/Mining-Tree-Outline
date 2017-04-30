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
with open(datadir + "/actor_hash.csv") as actorcsv:
	linereader = csv.reader(actorcsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split(":")
		actor = split_line[0]
		actor_id = split_line[1]
		cur.execute("UPDATE all_data SET actor_1_id = ? WHERE actor_1_id = ?" , (str(actor_id) , actor.decode("utf8")))
		cur.execute("UPDATE all_data SET actor_2_id = ? WHERE actor_2_id = ?" , (str(actor_id) , actor.decode("utf8")))
		cur.execute("UPDATE all_data SET actor_3_id = ? WHERE actor_3_id = ?" , (str(actor_id) , actor.decode("utf8")))
		
conn.commit()
