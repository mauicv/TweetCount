'''
Created on 21 Oct 2016

@author: mauicv
'''
import sys
import json
import tweepy 

class MyStreamListen(tweepy.StreamListener):    
  
    def __init__(self, limit, stats, api=None):
        super(MyStreamListen, self).__init__()
        self.num_tweets = 0
        self.limit=limit
        self.finish=False 
        self.stats=stats
        self.trackerValue=1
            
    def on_data(self,data):
        
        allTweetData=json.loads(data)
                
        if self.num_tweets>=self.limit: #return false if all tweets collected
            self.finish=True
            return False
        else:
            try:
                d=allTweetData['user']['followers_count']
                for tweetBin in self.stats.bins:                    
                    if d>=tweetBin["numFrom"] and d<=tweetBin["numTo"]:
                        self.num_tweets+=1
                        tweetBin["numInBin"]+=1
                        print(self.num_tweets)

                        if allTweetData['text'].startswith("RT @") == True:
                            tweetBin["numOfRetweets"]+=1
                        else:
                            tweetBin["numOfTweets"]+=1
                        break
                if self.num_tweets>self.trackerValue*1000:
                    #save file every 1000 tweets...
                    self.trackerValue+=1
                    print("saving...",self.trackerValue)
                    self.stats.save()
                    

            except:
                pass
        pass
    
    def on_error(self, status_code):
        if status_code == 420:
            self.finish=True
            self.stats.Save()
            print("Rate limits exceeded")
            #returning False in on_data disconnects the stream
            return False
        
        if status_code == 401:
            self.finish=True
            self.stats.Save()
            print("Authentication error")
            return False
        