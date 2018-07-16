'''
Created on 13 Feb 2017

@author: mauicv
'''
import tweepy 
from tweepy import OAuthHandler
from TweetCounter.MyStreamListen import MyStreamListen
from TweetCounter.Stats import Stats
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

    
def RequestTweets(limit,stats):
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    L=MyStreamListen(limit, stats)
    tries=0

    while not L.finish:
        tries=tries+1
        print("This is try number:", tries)
        stream = tweepy.Stream(auth, L)
        
        try:
            stream.filter(track=["the"])
        except:
            print("Error. Restarting Stream...")
            L.stats.save()
            time.sleep(5)
        
def Get_tweets():
    
    pass   

if __name__ == '__main__':
    
    TweetStats=Stats(10,2500)
    TweetStats.load()

    then = time.time() #Time before the operations start
    
    #RequestTweets(505028,TweetStats)
    RequestTweets(100,TweetStats)
    
    now = time.time() #Time after it finished
    
    #TweetStats.save()
    
    #TweetStats.load()
    #TweetStats.normalize()
    TweetStats.drawAll()

    print("It took: ", now-then, " seconds")
    pass

    #432529

        
    