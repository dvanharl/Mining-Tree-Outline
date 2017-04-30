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
dir_cur = con.cursor()
all_data_cur = con.cursor()


# os.chdir("actor_lists/")

dir_list = dir_cur.execute("SELECT * FROM director_id").fetchall()

people_not_found = []
try:
	dir_cur.execute("ALTER TABLE director_id ADD COLUMN director_rating 'TEXT' ")
except:
	pass	

with open(datadir+"/director_lists/director-a-list.csv") as directorcsv:
	a_contents = directorcsv.read()
with open(datadir+"/director_lists/director-b-list.csv") as directorcsv:
	b_contents = directorcsv.read()
with open(datadir+"/director_lists/director-c-list.csv") as directorcsv:
	c_contents = directorcsv.read()

# actor_list = actor_list.fetchall()

# raw_input(len(actor_list))

for dire in dir_list:
	dire_name = dire[0].encode("utf8")
	rating = "d"
	if dire == '':
		print "Skipping over the blank director"
		continue
	if dire_name +"," in a_contents:
		# print actor
		# actor_cur.execute("UPDATE actor_id SET actor_rating = ? WHERE actor_id = ?" , ("a" , actor[1]))
		rating = "a"
	elif dire_name +"," in b_contents:
		# print actor
		#actor_cur.execute("UPDATE actor_id SET actor_rating = ? WHERE ")
		rating = "b"
	elif dire_name + "," in c_contents:
		# print actor
		rating = "c"
	else:
		people_not_found.append(dire)
	# print rating
	# print actor[1]
	dir_cur.execute("UPDATE director_id SET director_rating = ? WHERE director_id = ?" , (rating , dire[1]))
	
con.commit()
