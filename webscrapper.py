from asyncio import constants
from operator import eq
import tweepy
import os
import json

from win_notification import WindowAlert
# import win_notification
# Variables for Keys and Tokens
localConsumerKey = None
localConsumerSecret = None
localAccessToken = None
localTokenSecret = None
localBearerToken = None

credentialFilePath = 'creds.txt'
secretsFilePath = 'secrets.txt'
bearerFilePath = 'bearer.txt'


def setAuthForTweepy():
    if os.path.isfile(credentialFilePath):
        with open(credentialFilePath) as f:
            global localConsumerKey, localConsumerSecret
            localConsumerKey = f.readline().strip()
            localConsumerSecret = f.readline().strip()
    f.close()


    if os.path.isfile(secretsFilePath):
        with open(secretsFilePath) as f:
            global localAccessToken, localTokenSecret
            localAccessToken = f.readline().strip()
            localTokenSecret = f.readline().strip()
    f.close()

    if os.path.isfile(bearerFilePath):
        with open(bearerFilePath) as f:
            global localBearerToken
            localBearerToken = f.readline().strip()


def setupTweepyClient():
    setAuthForTweepy()
    return tweepy.Client(localBearerToken,localConsumerKey,localConsumerSecret,localAccessToken,localTokenSecret)

def setupTweepyAPI():
    setAuthForTweepy()
    auth = tweepy.OAuthHandler(consumer_key=localConsumerKey, consumer_secret=localConsumerSecret)
    auth.set_access_token(localAccessToken, localTokenSecret)
    return tweepy.API(auth)

def monitorTwitterAccount(screen_name):
    api = setupTweepyAPI()
# pip install win10toast
    targeted_screen_name = screen_name
    user = api.get_user(screen_name = targeted_screen_name)
    print(user.id)
    client = setupTweepyClient()
    printer = TweetPrinter(localConsumerKey, localConsumerSecret, localAccessToken, localTokenSecret)
    printer.setTargetAccount(targeted_screen_name)
    printer.filter(follow = [user.id], filter_level='low')

class TweetPrinter(tweepy.Stream):
    targetAccount = ''
    twitterClient = ''
    notifyClass = None


    def setTargetAccount(self, target_account):
        global targetAccount, twitterClient, notifyClass
        targetAccount = target_account
        twitterClient = setupTweepyClient()
        notifyClass =  WindowAlert()

    def on_data(self, status):
        data = json.loads(status)
        
        user = data['user']['screen_name']
        tweet_id = data['id']
        tweet = twitterClient.get_tweet(id=tweet_id)

        if(user==targetAccount):
            notifyClass.MyNotification(str(tweet[0]))
            print(tweet[0])
