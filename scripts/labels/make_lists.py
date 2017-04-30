import csv
import os, os.path
import re

a_num = 800
b_num = 200
c_num = 0

curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
# datadir = os.path.abspath(os.path.join(pardir , "data/"))
datadir = pardir.replace("/scripts" , "/data")

# put the actors into lists
with open(datadir+"/actor-list.csv" , "r") as actorcsv:
	reader = csv.reader(actorcsv, delimiter = ",")
	a_list = ""
	b_list = ""
	c_list = ""
	for line in reader:
		# raw_input(line)
		gross = line[1]
		gross = re.sub("[$k]" , "" , gross)
		gross = float(gross)
		if gross > a_num:
			a_list += ((line[0] + ",") + (line[1] +"\n"))
		elif a_num - 1 > gross and gross > b_num:
			b_list += ((line[0] + ",") + (line[1] + "\n"))
		else:
			c_list += ((line[0] + ",") + (line[1] + "\n"))

with open(datadir+"/actor_lists/actor-a-list.csv" , "w") as acsv:
	acsv.write(a_list)

with open(datadir + "/actor_lists/actor-b-list.csv" , "w") as bcsv:
	bcsv.write(b_list)

with open(datadir + "/actor_lists/actor-c-list.csv" , "w") as ccsv:
	ccsv.write(c_list)

# put the directors into lists
with open(datadir+"/director-list.csv" , "r") as directorcsv:
	reader = csv.reader(directorcsv, delimiter = ",")
	a_list = ""
	b_list = ""
	c_list = ""
	for line in reader:
		# raw_input(line)
		gross = line[1]
		gross = re.sub("[$k]" , "" , gross)
		gross = float(gross)
		if gross > a_num:
			a_list += ((line[0] + ",") + (line[1] +"\n"))
		elif a_num - 1 > gross and gross > b_num:
			b_list += ((line[0] + ",") + (line[1] + "\n"))
		else:
			c_list += ((line[0] + ",") + (line[1] + "\n"))

with open(datadir+"/director_lists/director-a-list.csv" , "w") as acsv:
	acsv.write(a_list)

with open(datadir + "/director_lists/director-b-list.csv" , "w") as bcsv:
	bcsv.write(b_list)

with open(datadir+"/director_lists/director-c-list.csv" , "w") as ccsv:
	ccsv.write(c_list)





