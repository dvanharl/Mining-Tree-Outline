import os , os.path
import sqlite3

# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
datadir = os.path.abspath(os.path.join(pardir , "data/"))

conn = sqlite3.connect(datadir + "/data.db")
all_data_cur = conn.cursor()
movie_title_cur = conn.cursor()
# get the gross and the budget stuff

results = all_data_cur.execute('SELECT movie_id, gross, budget FROM all_data')

for row in results:
	print "This is the row " + str(row)
	# print typeof(row[0])
	movie_title = movie_title_cur.execute('SELECT movie_title FROM movie_id WHERE movie_id = (?)' , (row[0],) )
	print str(movie_title.fetchone())
	if '' not in row:
		# print "This is row: "
		x = float(row[1])
		y = float(row[2])
	
