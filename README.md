# Guitar_Tab_Recommender

# Problem:  
As a guitarist, I am always interested in learning new songs to play.  I rely primarily on guitar tablature files that I find online to learn how to play these new songs.  Many of the songs that I come across during my search are incompatible with my musical tastes or skill level.  Too often I spend more time searching for songs that I like to play than actually playing them.

# Challenge:  
My goals are to lessen the time spent searching for tabs as well as increase the quality and compatibility of tabs that are found, ultimately increasing both the quantity and quality of time spent playing the guitar.

# Solution:  
Build tab database from which tabs can be accessed
Obtain and store user ratings for the tabs in database
Recommendation system which suggests guitar tabs to a user based on his or her own preferences, as they relate to other users with similar preferences via collaborative filtering
Preliminary survey of broad preferences of users in order to generate initial ratings

# Modeling/Techniques:
Data Scraping from Ultimate-Guitar, a large online database of tabs, via Selenium and Beautiful Soup
Storing of information into MongoDB and Spark
Natural Language Processing for use in Sentiment Analysis to generate user ratings via NLTK Vader
Matrix Factorization via the Alternating Least Squares Method for Collaborative Filtering
Feature Engineering and Surveying strategies for cold starts
Interactive Desktop Application for use by unique users

# Further Steps: 
Continued collection of tabs and ratings
Further investigation into optimization of model parameters
Deployment of interactive website for wider access
Additional tuning of Sentiment Analysis model
Feature additions related to tab difficulty and skill level
