import glob
import os, os.path
import sqlite3

curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
# datadir = os.path.abspath(os.path.join(pardir , "data/"))
datadir = pardir.replace("/scripts" , "/data")


# raw_input(datadir)
con = sqlite3.connect(datadir + "/data.db")
actor_cur = con.cursor()
all_data_cur = con.cursor()


# os.chdir("actor_lists/")

actor_list = actor_cur.execute("SELECT * FROM actor_id").fetchall()

people_not_found = []
try:
	actor_cur.execute("ALTER TABLE actor_id ADD COLUMN actor_rating 'NUMERIC' ")
except:
	pass	

with open(datadir+"/actor_lists/actor-a-list.csv") as actorcsv:
	a_contents = actorcsv.read()
with open(datadir+"/actor_lists/actor-b-list.csv") as actorcsv:
	b_contents = actorcsv.read()
with open(datadir+"/actor_lists/actor-c-list.csv") as actorcsv:
	c_contents = actorcsv.read()

# actor_list = actor_list.fetchall()

# raw_input(len(actor_list))

for actor in actor_list:
	actor_name = actor[0].encode("utf8")
	rating = "d"
	if actor == '':
		print "Skipping over the blank actor"
		continue
	if actor_name +"," in a_contents:
		# print actor
		# actor_cur.execute("UPDATE actor_id SET actor_rating = ? WHERE actor_id = ?" , ("a" , actor[1]))
		rating = "a"
	elif actor_name +"," in b_contents:
		# print actor
		#actor_cur.execute("UPDATE actor_id SET actor_rating = ? WHERE ")
		rating = "b"
	elif actor_name + "," in c_contents:
		# print actor
		rating = "c"
	
	else:
		people_not_found.append(actor)
	# print rating
	# print actor[1]
	actor_cur.execute("UPDATE actor_id SET actor_rating = ? WHERE actor_id = ?" , (rating , actor[1]))
	
con.commit()
