from asyncio import constants
from operator import eq
import tweepy
import os
import json
import win_notification
# Variables for Keys and Tokens
localConsumerKey = None
localConsumerSecret = None
localAccessToken = None
localTokenSecret = None
localBearerToken = None

# Filepath where keys and tokens are located on local machine
credentialFilePath = 'creds.txt'
secretsFilePath = 'secrets.txt'
bearerFilePath = 'bearer.txt'
# only run if file exists
if os.path.isfile(credentialFilePath):
    with open(credentialFilePath) as f:
        localConsumerKey = f.readline().strip()
        localConsumerSecret = f.readline().strip()
    f.close()


if os.path.isfile(secretsFilePath):
    with open(secretsFilePath) as f:
        localAccessToken = f.readline().strip()
        localTokenSecret = f.readline().strip()
f.close()

if os.path.isfile(bearerFilePath):
    with open(bearerFilePath) as f:
        localBearerToken = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key=localConsumerKey, consumer_secret=localConsumerSecret)
auth.set_access_token(localAccessToken, localTokenSecret)

api = tweepy.API(auth)
targeted_screen_name = 'LeBlorstOfTimes'
user = api.get_user(screen_name = targeted_screen_name)
print(user.id)
client = tweepy.Client(localBearerToken,localConsumerKey,localConsumerSecret,localAccessToken,localTokenSecret)


# user_1 = client.get_user(username='towelthetank')
# print(user_1)
# print(user_1[:])

# tweet = client.get_users_tweets(id=123276343, exclude=['retweets', 'replies'], since_id='1488934019169411085')

# print(tweet)

# print(tweet[0])

# if localConsumerKey == None or localConsumerSecret == None:
#     os._exit(1) 



 
# print(user.id)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

class TweetPrinter(tweepy.Stream):

    def on_data(self, status):
        data = json.loads(status)
        
        user = data['user']['screen_name']
        tweet_id = data['id']
        tweet = client.get_tweet(id=tweet_id,)
        if(user==targeted_screen_name):
            win_notification.MyNotification(tweet[0])
            print(tweet[0])

printer = TweetPrinter(localConsumerKey, localConsumerSecret, localAccessToken, localTokenSecret)
printer.filter(follow = [user.id], filter_level='low')

# tweet = client.get_tweet(id=1488985196955418625)
# print(tweet[0])

