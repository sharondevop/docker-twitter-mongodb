from __future__ import print_function
import tweepy
import json
import os
from pymongo import MongoClient
 


# TODO
# Replace print with Logger
# Get word list from docker var list 
WORDS = ['#Docker']
 
#Retrieve & set environment variables
MONGO_HOST= os.environ.get('MONGO_HOST')     #'mongodb://localhost/twitterdb'  #Assuming you have mongoDB installed locally
                                             #and a database called 'twitterdb'
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API.
 
    def on_connect(self):
        #Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
    def on_error(self, status_code):
        #On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)
            
            #Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb
    
            #Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #Grab the 'user name' data from the Tweet to use for display
            user_name = datajson['user']['name']
            
            #print out a message to the screen that we have collected a tweet
            print("Tweet by user: " + str(user_name))
            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            db.twitter_search.insert(datajson)
        except Exception as e:
           print(e)
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
