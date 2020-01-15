import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#gets the movie data using fetch_movielens method of ratings = 4
data = fetch_movielens(min_rating=4.0)

#print the training and the testing data
print(repr(data['train']))
print(repr(data['test']))

#make the model
model = LightFM(loss='warp') #warp stands for weighted approximate-rank pairwise
#train the model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, usr_ids):

	#number of users and movies that are in the training data
	num_users, num_items = data['train'].shape

	#create recommendations for each user
	for user_id in usr_ids:

		#list of movies the user already likes
		known_positives_list = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#using our model, we predict what movies the the user will like
		movie_prediction = model.predict(user_id, np.arrange(num_items))

		#lists the recommended movies in descending order
		top_ranking_items = data['item_labels'][np.argsort(-movie_prediction)]

		#print out the top 3 movies from the known positives movie list
		print("User %s" % user_id)
		print("Known positives: (top 3 movies)")

		for known_positive_movie in known_positives_list[:3]:
			print("%s" % known_positive_movie)

		#print out top 3 recommended movies 
		print("Recommended Movies: ")

		for recommended_movie in top_ranking_items[:3]:
			print("%s" % recommended_movie)

#calling the sample recommendation function
sample_recommendation(model, data, [43, 64, 423])










