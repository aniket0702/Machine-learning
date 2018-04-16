# User Authentication

import tweepy
from tweepy import OAuthHandler

consumer_key = 'I42nPDOyzs6UckRFy1QxtsPf8'
consumer_secret = 'jmCre6s2MnWPbgZWAUjGhAXIoUwnm4sqBISdjvsc9itakzwnNG'
access_token = '756314704755105796-75NOLBnpEk9xmdqm4ml5JzHR6pMDOJ8'
access_secret = 'RyZrHSqpZohkd090Ufw08KcfuFwcU4rU1INDA3zV13yD2'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)


# for friend in tweepy.Cursor(api.friends).items():
#     print (friend)

# Using hashtags to store data in a json file



from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                # print data
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])