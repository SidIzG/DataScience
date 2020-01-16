# DataScience

# 1. Gender Classifier

For this project, I predicted the genders of people based on their height and weight using machine learning. I used the sklearn library for machine learning. I provided my machine learning model a data set with contained the height and weight of a person and their corressponding gender. The model is trained on that data and so I am able to predict a person's gender based on their height and weight.

# 2. Twitter Sentiment Analysis:

During the development of this project, I used the tweepy API to connect to Twitter and the textblob library for NLP. After authenticating with twitter, I search for a keyword/keyphrase. My goal is to see if the topic has a positive or a negative connotation to it. I made an empty list, and added the polarity of each tweet that has the keyword or key phrase. Then I took the average of that list which gives me the overall sentiment about the topic.

# 3. Movie Recommendation System

My project takes in a dataset of movies and their ratings. Then based on those ratings, the program will use machine learning recommend other similar movies that a user may like using the lightfm library. I used lightfm's fetch_movielens method to get all the movies with a rating of 4 and above. In my program, I print out the top 3 movies that I know of from the list of movies, and I then I print out 3 recommended movies for the user.  

# 4. Deep dream art

For this project, I replicated Google's Deep Dream neural network using Tensorflow to create some cool art using an existing image. I had to make extensive use of the TensorFlow library. I used google's pre-trained neural network called Inception. Then I created a TensorFlow session, chose a layer within the pre-trained network to enhance the image, and lastly I applied the Gradient Ascent Algoritm to the chosen layer.    

# 5. Genetic algoritm

In this project, I used Genetic programming to identify if some energy is Gamma radiation or not. I used the 3 steps of genetic programming: Selection, Crossover, and Mutation. I used data coming from the Cherenkov telescope which is a russian telescope that measures radiation. I had to clean the data, split the data into training, testing, and validation data. Then I used the tpot library to train our model, compute the testing error for validation, and lastly export the code to the "pipeline.py" class.  
