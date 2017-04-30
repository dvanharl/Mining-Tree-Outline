import os , os.path
import sqlite3


# Get the path for the database
curpath = os.path.abspath(__file__)
curdir = os.path.abspath(os.path.join(curpath , os.pardir))
pardir = os.path.abspath(os.path.join(curdir , os.pardir))
datadir = pardir.replace("/scripts" , "/data")


conn = sqlite3.connect(datadir + "/data.db")
cur = conn.cursor()
cur.execute("SELECT * from sqlite_master WHERE type = 'table';")
results = cur.fetchone()
all_data_schema= results[4]

cur.execute('ALTER TABLE all_data RENAME TO all_data_temp')

# print all_data_schema

# Change the table name
# all_data_schema = all_data_schema.replace('''all_data''' , '''all_data_temp''')

# Change the directors to numeric and ids
all_data_schema = all_data_schema.replace('''"director_name" TEXT''' , '''director_id NUMERIC''')

# Change the 3 actors to numeric and ids
all_data_schema = all_data_schema.replace('''"actor_1_name" TEXT''' , '''actor_1_id NUMERIC''')
all_data_schema = all_data_schema.replace('''"actor_2_name" TEXT''' , '''actor_2_id NUMERIC''')
all_data_schema = all_data_schema.replace('''"actor_3_name" TEXT''' , '''actor_3_id NUMERIC''')

# Change the movie title
all_data_schema = all_data_schema.replace('''"movie_title" TEXT''' , '''movie_id NUMERIC''')

# print all_data_schema

# Change the budget and gross to numeric values
all_data_schema = all_data_schema.replace('''"gross" TEXT''' , '''gross NUMERIC''')
all_data_schema = all_data_schema.replace('''"budget" TEXT''' , '''budget NUMERIC''')

# Change the duration and years to a numeric value
all_data_schema = all_data_schema.replace('''"duration" TEXT''' , '''duration NUMERIC''')
all_data_schema = all_data_schema.replace('''"title_year" TEXT''' , '''title_year NUMERIC''')


# This is the new schema we want
# print all_data_schema

# Create and import, then delete
cur.execute(all_data_schema)
cur.execute('''INSERT INTO all_data SELECT * from all_data_temp''') 
cur.execute('''DROP TABLE all_data_temp''')


conn.commit()

# cur.execute('ALTER TABLE all_data_temp RENAME TO all_data')
