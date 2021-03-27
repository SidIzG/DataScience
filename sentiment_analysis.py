import tweepy
from statistics import mean
from textblob import TextBlob

#these variables are what are required to authenticate with twitter

consumer_key = 'J0PAX4EPr58W5ZKWeixhCd9Ka'
consumer_secret = 'IptCGN7iDH57CgvajAwMhkvpTT6fIgq18DX73h5EZ5yj10wRB6'

access_token = '1213222796219707392-NbiUNkSba0Nh9CI8cHswis8lq6T4Kh'
access_token_secret = 'dqj8803zvZS8hiPMbcKDUaIjMr1W8n8M7274ThbumurD1'

#authenticating with twitter (login with code)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#main variable which we can use to access twitter methods
twitter_api = tweepy.API(auth)

#this method will return tweets that contain the search argument
public_tweets = twitter_api.search("Arnold Schwarzenegger")

polarity_list = []

#This is where the sentiment analysis is done on each tweet
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#analysis.sentiment will return polarity and subjectivity
	#Polarity is how positive or negative something is
	#Subjectivitity is how much of an opinion something is vs factual. How opinionated the text is
	
	#print(analysis.sentiment)
	print(analysis.sentiment.polarity)
	polarity_list.append(analysis.sentiment.polarity)
	print("\n")

#This makes takes the average of the list of polarities
average_polarity = mean(polarity_list)

#This tells us if the topic/word is overall a positive or negative thing
if average_polarity < 0:
	print("This is a negative topic currently")
elif average_polarity > 0:
	print("This is a positive topic currently")
