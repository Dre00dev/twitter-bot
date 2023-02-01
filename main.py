# Create a bot that will post motivational quotes and retweet content related to Tech throughout the day
# Goal is to create a project that fully automated and won't need to be run 

# When using replit, heroku, or Railways must put your keys in the .env file

import tweepy 
import requests
import json
import schedule
import time
import logging

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key",
    "consumer_secret")
auth.set_access_token("access_token",
    "secret_access_token")

api = tweepy.API(auth)

#ZEN QUOTES RANDOMIZED 
def getQuote():
    response = requests.get("https://zenquotes.io/api/random")  #returns random quote
    jsonData = json.loads(response.text)    #loads response as json
    # q is key for quote a is key for author
    quote = jsonData[0]['q'] + " -" + jsonData[0]['a']
    return(quote)

def getTech():
    search = tweepy.Cursor(api.search_tweets, q = "Python", lang = "en").items(1) #search will return 1 'tweet' object
    return([tweet.text for tweet in search])     
    

def tweetQuote():
    quote = getQuote()
    api.update_status(quote)
    #print(quote)

def tweetTech():
    tech = getTech()
    api.update_status(tech)
    #print(tech)

def Scheduler():
    schedule.every().hour.at(":00").do(tweetQuote)
    schedule.every().hour.at(":30").do(tweetTech)
    while True:
        schedule.run_pending()
        time.sleep(1)


Scheduler()






