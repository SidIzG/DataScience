# DataScience

For the Twitter Sentiment Analysis, I used the tweepy API to connect to Twitter and the textblob library for NLP.
<img width="550" alt="Screen Shot 2020-01-07 at 7 48 48 PM" src="https://user-images.githubusercontent.com/33462891/71945561-2a6e9600-3195-11ea-8208-5aa9aa12cf6b.png">

After authenticating with twitter, I search for a keyword/keyphrase. In my case, I looked up "Arnold Schwarzenegger"
<img width="470" alt="Screen Shot 2020-01-08 at 10 47 21 PM" src="https://user-images.githubusercontent.com/33462891/72036459-ebaa1000-3268-11ea-8e42-4faaae869c16.png">

After that, I want to see the average polarity of how that particular topic is viewed. So I made an empty list, and added the polarity of each tweet that has the keyword or key phrase. It checks the sentiment of it, and then appends the polarity to the empty list.

<img width="757" alt="Screen Shot 2020-01-08 at 10 46 59 PM" src="https://user-images.githubusercontent.com/33462891/72036483-f95f9580-3268-11ea-9e3b-15b1e10beb03.png">


When I run the code, I see whether the keyword: "Arnold Schwarzenegger" has a positive or a negative sentiment in the Twitter community

<img width="570" alt="Screen Shot 2020-01-08 at 10 52 47 PM" src="https://user-images.githubusercontent.com/33462891/72036728-beaa2d00-3269-11ea-97ff-d628ad95ad5f.png">
