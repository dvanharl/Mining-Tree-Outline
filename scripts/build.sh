
folder=$PWD

# echo "Renaming the tables and fixing the values"
# scp "$folder/scripts/rename/rename_complete.py" .
# python "$folder/scripts/rename/rename_complete.py"
# sleep .5

echo "Creating the actor ids and saving them"
# scp "$folder/scripts/actors/actors_complete.py" .
python "$folder/scripts/actors/actors_complete.py"

echo "Creating the director ids and saving them"
# scp "$folder/scripts/directors/directors_complete.py" .
python "$folder/scripts/directors/directors_complete.py"

echo "Creating the movie ids and saving them"
# scp "$folder/scripts/movies/movies_complete.py" .
python "$folder/scripts/movies/movies_complete.py"

echo "Creating the success ratios and saving them"
python "$folder/scripts/success_ratio/success_ratio.py"

echo "Creating the success attribute"
python "$folder/scripts/success_ratio/success.py"

echo "Labeling the actors and the directors  "
python "$folder/scripts/labels/make_lists.py"
python "$folder/scripts/labels/label_dirs.py"
python "$folder/scripts/labels/label_actors.py"
python "$folder/scripts/labels/add_labels.py"


echo "Bucketing the values"
python "$folder/scripts/buckets/make_buckets.py"


# python "$folder/scripts/rename_complete.py"
# rm "$folder/scripts/rename_complete.py"

# for d in */ ; do
#	scp $d/*.py .
#	for f in *.py ; do
#		python "$f"
#	done
#done	

