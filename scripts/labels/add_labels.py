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
actor_cur = conn.cursor()
director_cur = conn.cursor()
data_cur = conn.cursor()

actor_results = actor_cur.execute("SELECT actor_id , actor_rating FROM actor_id")
director_results = director_cur.execute("SELECT director_id , director_rating FROM director_id")

try:
	data_cur.execute("ALTER TABLE all_data ADD COLUMN actor_1_rating 'TEXT'  ")
	data_cur.execute("ALTER TABLE all_data ADD COLUMN actor_2_rating 'TEXT' ")
	data_cur.execute("ALTER TABLE all_data ADD COLUMN actor_3_rating 'TEXT' ")
	data_cur.execute("ALTER TABLE all_data ADD COLUMN director_rating 'TEXT' ")
except:
	pass

for row in actor_results.fetchall():
	actor_tup = (row[1] , row[0])
	data_cur.execute("UPDATE all_data SET actor_1_rating = ? WHERE actor_1_id = ?" , actor_tup)
	data_cur.execute("UPDATE all_data SET actor_2_rating = ? WHERE actor_2_id = ?" , actor_tup)
	data_cur.execute("UPDATE all_data SET actor_3_rating = ? WHERE actor_3_id = ?" , actor_tup)

for row in director_results.fetchall():
	director_tup = (row[1] ,row[0])
	data_cur.execute("UPDATE all_data SET director_rating = ? WHERE director_id = ?" , director_tup)
	
conn.commit()


