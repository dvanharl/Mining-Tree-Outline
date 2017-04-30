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
datadir = pardir.replace("/tree" , "/data")

# print datadir
conn = sqlite3.connect(datadir + "/data/data.db")
cur = conn.cursor()

def get_data():
	select_attr = ""
	with open("tree/attr.txt" , "r") as attr:
		select_attr = attr.read().replace("\n" , ",").rstrip(",")
	
	directors_b = 0
	actor_1_b = 0
	actor_2_b = 0
	actor_3_b = 0

	if "director_id" in select_attr:
		directors_b = 1
	if "actor_1_id" in select_attr:
		actor_1_b = 1
	if "actor_2_id" in select_attr:
		actor_2_b = 1
	if "actor_3_id" in select_attr:
		actor_3_b = 1

	statement = "SELECT " + select_attr + " FROM all_data WHERE success NOT LIKE '%,None,%'    "
	results = cur.execute(statement).fetchall()
	write_to_csv(select_attr, results)
	
	data_to_use = results
	return data_to_use , select_attr.split(",")

def write_to_csv(headers, results):
	print "Writing to csv file for usage with weka"
	with open("weka/data.csv" , "w") as csvfile:
		csvfile.write(headers+"\n")
		for row in results:
			string_to_build = ""
			for attr in row:
				if not type(attr) is int:
					string_to_build += (str(attr.encode("utf8")) + ",")
				string_to_build += (str(attr) +",")
			string_to_build = (string_to_build.rstrip(",")) + "\n"
			string_to_build  = string_to_build.replace("'" , "")
			csvfile.write(string_to_build.lstrip(" "))


