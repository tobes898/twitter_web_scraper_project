import tweepy
import os
import json

from win_notification import WindowAlert
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

# Deprecating old V1.1 code method
# def setupTweepyAPI():
#     setAuthForTweepy()
#     auth = tweepy.OAuthHandler(consumer_key=localConsumerKey, consumer_secret=localConsumerSecret)
#     auth.set_access_token(localAccessToken, localTokenSecret)
#     return tweepy.API(auth)

def monitorTwitterAccount(screen_name):
    targeted_screen_name = screen_name

    # Old V1.1 Code
    # api = setupTweepyAPI()
    # user = api.get_user(screen_name = targeted_screen_name)
   

    client = setupTweepyClient()
    user = client.get_user(username=screen_name)
    printer = TweetPrinter(localConsumerKey, localConsumerSecret, localAccessToken, localTokenSecret)
    printer.setTargetAccount(targeted_screen_name)
    print(user.data['id'])
    printer.filter(follow = [user.data['id']], filter_level='low')

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



# getMultipleTimelines - takes in list of users and number of tweets to return for each
# starting with the most recent. numOfTweets defaults to 5 if no value given
def getMultipleTimelines(users, numOfTweets=5):
    client = setupTweepyClient()
    # return a list of users
    user_data = client.get_users(usernames=users)
    for user in user_data.data:
        #TODO: might not be necessary, decide on this later
        tweets = client.get_users_tweets(id=user['id'], max_results=numOfTweets)
        num = 1
        print(user['username'] + '\n__________')
        for tweet in tweets.data:
            print(str(num) + ':' + tweet['text'])
            num+=1
