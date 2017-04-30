folder=$PWD

echo "Gathering actor information"
python "$folder/scraper/actor_gross_scraper.py"

sleep 1

echo "Gathering director information"
python "$folder/scraper/director_gross_scraper.py"

sleep 1

echo "Finished Gathering!"

