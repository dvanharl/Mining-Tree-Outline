import os , os.path
import sqlite3

#Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))

#datadir = os.path.abspath(os.path.join(pardir , "data/"))
datadir = pardir.replace("/scripts" , "/data")
conn = sqlite3.connect(datadir + "/data.db")
all_data_cur = conn.cursor()
# movie_title_cur = conn.cursor()

#raw_input(datadir)

#Get the success ratio
results  = all_data_cur.execute("SELECT movie_id, ratio FROM all_data").fetchall()

#Alter table to include sucess binary attribute
try:
	all_data_cur.execute("ALTER TABLE all_data ADD COLUMN success 'TEXT'")
except:
	pass
for row in results:
	# print "This is the row " + str(row)
	#print typeof(row[0])
	# movie_title = movie_title_cur.execute('SELECT movie_title FROM movie_id = (?)' , (row[0]))
	# print str(movie_title.fetchone())
	if '' not in row and (not row[1] is None):
		# print "This is row: "
		# raw_input(row[1])
		rat = float(row[1])
		if rat >= 1.1:
			rat = "yes"
		else:
			rat = "no"
		all_data_cur.execute('''UPDATE all_data SET success = ? WHERE movie_id = ?''', (str(rat) , row[0]))
conn.commit()
		
