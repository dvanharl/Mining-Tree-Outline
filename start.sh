if [[ ! -f data/data.db ]] ; then
	echo "Creating the database"
	echo "."
	sleep .5
	echo "."
	sleep .5
	echo "."
	sleep .5
	sqlite3 data/data.db < data/create.sql

else
	echo "Database already created"

fi 

echo "Preprocess the data? (1 for yes, 0 for no)"
read preprocess

if  (( ("$preprocess" == "1" ) )) ; then
	echo "Proceeding to preprocess the data"
	if [[ ! -d data/actor_lists ]] ; then
		echo "Proceeding to gather information about actors and directors"
		./scraper/scraper.sh
	else
		echo "Actor labels are already found"
	fi
	

	echo "Running all the scripts"
	./scripts/build.sh
	

	echo "Proceeding to label the actors"
	
else 
	echo "Continuing to the analysis stage"
	./tree/analysis.sh
fi




echo "Tool Finished!"
