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

actor_hash = {}
actor_id = 0

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
