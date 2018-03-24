import tweepy

import json
import twitterconfig

# Twitter API Keys
consumer_key = twitterconfig.consumer_key
consumer_secret = twitterconfig.consumer_secret
access_token = twitterconfig.access_token
access_token_secret = twitterconfig.access_token_secret

# Setup Tweepy API Authentication

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# Send tweets every 60 Seconds to your homepage
tweet_num = 1
while tweet_num < 6:
   api.update_status("Tweet Number :" + str(time.ctime()) + " counter: " + str(tweet_num))
   tweet_num = tweet_num + 1
   time.sleep(60)