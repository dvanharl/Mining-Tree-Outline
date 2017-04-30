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
cur = conn.cursor()

results = cur.execute("SELECT budget FROM all_data")

vals = []
# put all the budget vals in to array
for row in results.fetchall():
	budget = row[0]
	if not budget ==  u'':
		vals.append(budget)

# sort the array
vals = sorted(list(set(vals)))

mid_index = int(len(vals) /2 )
min_mid_index = int(len(vals) / 4)
max_mid_index = int(len(vals[mid_index:len(vals)]) /2) + mid_index

min_mid = vals[min_mid_index]
max_mid = vals[max_mid_index]
mid = vals[mid_index]

#print "<" + str(min_mid)
#print str(min_mid) + "<x<" + str(mid)
#print str(mid) + "<x<" + str(max_mid)
#print str(max_mid) + "<"

try:
	cur.execute("ALTER TABLE all_data ADD COLUMN budget_class 'TEXT'")
except:
	pass

#one_count= 0
#two_count= 0
#three_count= 0
#four_count= 0

results = cur.execute("SELECT movie_id , budget from all_data")
for row in results.fetchall():
	
	budget = row[1]
	budget_class = -1
	
	if not budget == u'':
		if budget <= min_mid:
			budget_class = "budget <= " + str(min_mid)
			# one_count+=1
		elif min_mid < budget and budget <= mid:
			budget_class = str(min_mid) + " < budget <= " + str(mid)
			# two_count+=1
		elif mid < budget and budget <= max_mid:
			budget_class = str(mid) + " < budget <= " +str(max_mid)
			# three_count+=1
		elif max_mid < budget:
			# four_count+=1
			budget_class = str(max_mid) + " < budget"
		else:
			raw_input("It should not get here, click enter twice to continue")
			raw_input(budget)

	cur.execute("UPDATE all_data SET budget_class = ? WHERE movie_id = ?" , (budget_class , row[0]))

# print one_count
# print two_count
# print three_count
# print four_count


## BASICALLY A REPEAT OF ABOVE ##
years_q = cur.execute("SELECT title_year FROM all_data").fetchall()
dur_q = cur.execute("SELECT duration FROM all_data").fetchall()

years = []
durs = []
for row in years_q:
	years.append(row[0])
for row in dur_q:
	durs.append(row[0])

years = sorted(list(set(years)))
durs = sorted(list(set(durs)))

mid_index_y = int(len(years) /2 )
min_mid_index_y = int(len(years) / 4)
max_mid_index_y = int(len(years[mid_index_y:len(years)]) /2) + mid_index_y

min_mid_y = years[min_mid_index_y]
max_mid_y = years[max_mid_index_y]
mid_y = years[mid_index_y]


mid_index_d = int(len(durs) /2 )
min_mid_index_d = int(len(durs) / 4)
max_mid_index_d = int(len(durs[mid_index:len(durs)]) /2) + mid_index_d

min_mid_d = durs[min_mid_index_d]
max_mid_d = durs[max_mid_index_d]
mid_d = durs[mid_index_d]

# year part first
try:
	cur.execute("ALTER TABLE all_data ADD COLUMN year_class 'TEXT'")
except:
	pass 

results = cur.execute("SELECT movie_id ,title_year from all_data")
for row in results.fetchall():
	
	title_year = row[1]
	year_class = -1

	
	if not title_year == u'':
		if title_year <= min_mid_y:
			year_class =  "title_year <= " + str(min_mid_y)
			# one_count+=1
		elif min_mid_y < title_year and title_year <= mid_y:
			year_class = str(min_mid_y) + " < title_year <= " + str(mid_y) 
			# two_count+=1
		elif mid_y < title_year and title_year <= max_mid_y:
			year_class = str(mid_y) + " < title_year <= " + str(max_mid_y)
			# three_count+=1
		elif max_mid_y < title_year:
			# four_count+=1
			year_class = str(max_mid_y) + " < title_year" 
		else:
			raw_input("It should not get here, click enter twice to continue")
			raw_input(title_year)

	cur.execute("UPDATE all_data SET year_class = ? WHERE movie_id = ?" , (year_class , row[0]))

# Now for the duration stuff
try:
	cur.execute("ALTER TABLE all_data ADD COLUMN dur_class 'TEXT'")
except:
	pass 

results = cur.execute("SELECT movie_id ,duration from all_data")
for row in results.fetchall():
	
	dur = row[1]
	dur_class = -1
	
	if not dur == u'':
		if dur <= min_mid_d:
			dur_class = "duration <= " + str(min_mid_d)
			# one_count+=1
		elif min_mid_d < dur and dur <= mid_d:
			dur_class = str(min_mid_d) + " < duration <= " + str(mid_d)
			# two_count+=1
		elif mid_d < dur and dur <= max_mid_d:
			dur_class = str(min_d) + " < duration <= " + str(max_mid_d)
			# three_count+=1
		elif max_mid_d < dur:
			# four_count+=1
			dur_class = str(max_mid_d) + " < duration "
		else:
			raw_input("It should not get here, click enter twice to continue")
			raw_input(dur)

	cur.execute("UPDATE all_data SET dur_class = ? WHERE movie_id = ?" , (dur_class , row[0]))



# print "<" + str(min_mid_d)
# print str(min_mid_d) + "<x<" + str(mid_d)
# print str(mid_d) + "<x<" + str(max_mid_d)
#:print str(max_mid_d) + "<"

results = cur.execute("SELECT genres FROM all_data")
genres_q = results.fetchall()

genres = []
for row in genres_q:
	genres.append(row[0].split("|")[0] if "|" in row[0] else row[0])


genres = list(set(genres))

genres_hash = {}
count  = 1
for genre in genres:
	genres_hash[genre] = count
	count+=1


try:
	cur.execute("ALTER TABLE all_data ADD COLUMN genre_class 'TEXT' ")
except:
	pass

results = cur.execute("SELECT movie_id , genres FROM all_data")
genres_q = results.fetchall()
for row in genres_q:
	genre = row[1].split("|")[0] if "|" in row[1] else row[1]
	# genre_class = genres_hash[genre]
	cur.execute("UPDATE all_data SET genre_class = ? WHERE movie_id = ?" , (genre, row[0]))





# print len(list(set(years)))
# print len(list(set(durs)))



conn.commit()


