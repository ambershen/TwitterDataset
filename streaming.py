#!/bin/sh

#  streaming.py
#  
#
#  Created by Amber Shen on 15/6/3.
#
import tweepy
import csv
import random
import sys

#setting up Twitter API
consumer_key = ' '
consumer_secret = ' '
access_key = ' '
access_secret = ' '

#method to get a user's tweets
#def get_tweets(id_str):
   
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
    

def get_tweets(username):
    
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
   
	number_of_tweets = 500
    
	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)
    
	#create array of tweet information: username, tweet id, date/time, text
	tweets_for_csv = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
    
	#write to a new csv file from the array of tweets
	print "writing to {0}_tweets.csv".format(username)
	with open("{0}_tweets.csv".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter='|')
		writer.writerows(tweets_for_csv)

def followee_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    #get followee ids
    friends = api.friends_ids(username)
    for friend in friends:
        number_of_tweets = 180
        tweets = api.user_timeline(id = friend, count = number_of_tweets)
        tweets_for_csv = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
        print"writing to {0}_followee_tweets.csv".format(username)
        with open("{0}_followee_tweets.csv".format(username), 'w+') as file:
            writer = csv.writer(file, delimiter = '|')
            writer.writerows(tweets_for_csv)



if __name__ == '__main__':
    
    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
        followee_tweets(sys.argv[1])
    else:
        print "Error: enter one username"
