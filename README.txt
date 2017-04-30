Hi!

Basic Usage:
	To run the tool, use ./start.sh
	It will as you if you would like to preprocess, pick 1 or 0 to select your choice
	
	To delete the database to restart use ./restart.sh



** NOTE ** 
Running any of the scripts in the scripts folder will not work.
They were used to preprocess the data and are only left in to
show work done. They have no practice usage for analysis
** NOTE **


This project was written by David and Ameer

We used a dataset we found off of Kaggle
The dataset included the following attributes for over 5000 movies:
'color'
'director_name'
'num_critic_for_reviews'
'duration'
'director_facebook_likes'
'actor_3_facebook_likes'
'actor_2_name'
'actor_1_facebook_likes'
'gross'
'genres'
'actor_1_name'
'movie_title'
'num_voted_users'
'cast_total_facebook_likes'
'actor_3_name'
'facenumber_in_poster'
'plot_keywords'
'movie_imdb_link'
'num_user_for_reviews'
'language'
'country'
'content_rating'
'budget'
'title_year'
'actor_2_facebook_likes'
'imdb_score'
'aspect_ratio'
'movie_facebook_likes'

The data was formatted to have director and actor names changed to be associated with a unique id.
For our analysis, we decided to focus on the following attributes:

'director_name'
'duration'
'director_facebook_likes'
'actor_3_facebook_likes'
'actor_2_name'
'actor_1_facebook_likes'
'genres'
'actor_1_name'
'movie_title'
'num_voted_users'
'cast_total_facebook_likes'
'actor_3_name'
'facenumber_in_poster'
'plot_keywords'
'movie_imdb_link'
'language'
'country'
'content_rating'
'budget'
'title_year'
'actor_2_facebook_likes'

These entries are listed in the filtered_attr table
