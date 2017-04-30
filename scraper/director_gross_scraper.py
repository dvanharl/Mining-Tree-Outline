import csv
from bs4 import BeautifulSoup
import urllib
import os
import time


curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
# datadir = os.path.abspath(os.path.join(pardir , "data/"))
# raw_input(pardir)
datadir = pardir.replace("/scraper" , "/data")

seen = [False for x in range(0 , 868)]



# raw_input(datadir +"actor-list.csv")
with open(datadir + "/data/director-list.csv" , "w") as csvfile:
	new_line = 0	
	for index in range(1 , 18):
		page = str(index)
		url = "http://www.boxofficemojo.com/people/?view=Director&pagenum="+page+"&sort=sumgross&order=DESC&&p=.htm"
		
		response = urllib.urlopen(url).read()
		# raw_input(response)

		soup = BeautifulSoup(response)
	
		tables = soup.findChildren('table')[2]
		rows  = tables.findChildren('tr')[0]
		vals = rows.findChildren('tr')[1:]
	
		for val in vals:
			string_to_write = ""
			entries = val.findChildren('font')
			index = int(entries[0].get_text())
			
			director_tag = entries[1].findChildren('b')
			director = director_tag[0].get_text()
			director = director.encode('utf8')			

			gross_tag = entries[2].findChildren('b')
			gross = gross_tag[0].get_text()
			gross = gross.encode('utf8')
			try:
				if not seen[index]:
					#raw_input(index)
					#raw_input(actor)
					#raw_input(gross)
					seen[index] = True
					string_to_write += (director.replace("," , "") + "," + gross.replace("," , "") + "\n" )
			
					csvfile.write(string_to_write)
			except:
				raw_input(director)
				raw_input(index)
			else:
				continue
		print "Waiting"
		time.sleep(1)
