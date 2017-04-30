import os , os.path
import sqlite3
import csv

# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
# datadir = os.path.abspath(os.path.join(pardir , "data/"))

datadir = pardir.replace("/scripts" , "/data")

conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

actor_hash = {}
actor_id = 0

try:
	cur.execute("ALTER TABLE all_data ADD COLUMN actor_1_id 'NUMERIC'")
	cur.execute("ALTER TABLE all_data ADD COLUMN actor_2_id 'NUMERIC'")
	cur.execute("ALTER TABLE all_data ADD COLUMN actor_3_id 'NUMERIC'")
except:
	pass



# Build the hash
# gather the 1st actors
for row in cur.execute('SELECT actor_1_name FROM all_data'):
	# raw_input(row)
	actor = u''.join((row[0])).encode('utf8').strip()
	try: 
		actor_hash[actor]
	except KeyError:	
		actor_hash[actor] = actor_id
		actor_id += 1


# gather the 2nd actors
for row in cur.execute("SELECT actor_2_name FROM all_data"):
	actor = u''.join((row[0])).encode('utf8').strip()
	try:
		actor_hash[actor]
	except KeyError:
		actor_hash[actor] = actor_id
		actor_id += 1

# gather the 3rd actors
for row in cur.execute('SELECT actor_3_name FROM all_data'):
	actor = u''.join((row[0])).encode('utf8').strip()
	try:
		actor_hash[actor]
	except KeyError:
		actor_hash[actor] = actor_id
		actor_id += 1

# Save it to the csv file		
with open(datadir + "/actor_hash.csv" , "w") as actor_file:
	string = ""
	for actor, actor_id in actor_hash.items():
		string += actor+":"
        	string += str(actor_id)
        	string += "\n"
 	actor_file.write(string)		

## Saves the csv into the database

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


## Update the values

conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()

# rename the row to actor id 


# Get the director relationships
with open(datadir + "/actor_hash.csv") as actorcsv:
	linereader = csv.reader(actorcsv , delimiter = "\n")
	for line in linereader:
		split_line = line[0].split(":")
		actor = split_line[0]
		actor_id = split_line[1]
		cur.execute("UPDATE all_data SET actor_1_id = ? WHERE actor_1_name = ?" , (str(actor_id) , actor.decode("utf8")))
		cur.execute("UPDATE all_data SET actor_2_id = ? WHERE actor_2_name = ?" , (str(actor_id) , actor.decode("utf8")))
		cur.execute("UPDATE all_data SET actor_3_id = ? WHERE actor_3_name = ?" , (str(actor_id) , actor.decode("utf8")))
		
conn.commit()

