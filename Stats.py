'''
Created on 20 Jun 2018

@author: mauicv
'''

import math
import matplotlib.pyplot as plt

import json


class Stats(object):
    
    def __init__(self,binSize,upperLimit):
        
        self.binSize=binSize
        self.numberOfBins=math.ceil(upperLimit/binSize)
        
        self.bins=[{'numInBin':0,
                    'density':0, 
                    'numOfTweets':0, 
                    'numOfRetweets':0,
                    'numFrom':val*binSize,
                    'numTo':(val+1)*binSize} for val in range(self.numberOfBins)]
        
    def draw(self):
        
        y=[tweetBin['numInBin'] for tweetBin in self.bins]
        x=[val*self.binSize for val in range(self.numberOfBins)]
        
        plt.bar(x,y, align='center',width=self.binSize, alpha=0.5)
        plt.xlim(0,self.binSize*self.numberOfBins)
        plt.xlabel('Number of Followers')
        plt.ylabel('Number of Users')

        plt.show()

        
    def drawRatios(self):
        
        y=[]
        x=[]
        
        for tweetBin in self.bins:
            if tweetBin['numInBin']!=0:
                y.append(tweetBin['numOfTweets']/tweetBin['numInBin'])
            else:
                y.append(0)
        x=[val*self.binSize for val in range(self.numberOfBins)]
        
        plt.bar(x,y, align='center',width=self.binSize, alpha=0.5)
        plt.xlim(0,self.binSize*self.numberOfBins)

        plt.show()

    def drawDensity(self):
        y=[tweetBin['density'] for tweetBin in self.bins]
        x=[val*self.binSize for val in range(self.numberOfBins)]
        
        plt.bar(x,y, align='center',width=self.binSize, alpha=0.5)
        plt.xlim(0,self.binSize*self.numberOfBins)
        plt.xlabel('Number of Followers')
        plt.ylabel('Density of Users')

        plt.show()

    def drawAll(self):
        
        xAxis=[val*self.binSize for val in range(self.numberOfBins)]
        tweetNums=[tweetBin['numInBin'] for tweetBin in self.bins]
        
        ratioNums=[]
        
        for tweetBin in self.bins:
            if tweetBin['numInBin']!=0:
                ratioNums.append(tweetBin['numOfTweets']/tweetBin['numInBin'])
            else:
                ratioNums.append(0)
        
        plt.subplot(2, 1, 1)
        plt.bar(xAxis, tweetNums, align='center',  width =10, alpha=0.5)
        plt.title('Tweets to Retweets')
        plt.ylabel('Number of users')
        
        plt.xlim(0,self.binSize*self.numberOfBins)

        
        plt.subplot(2, 1, 2)
        plt.bar(xAxis, ratioNums, align='center', width =10,alpha=0.5)
        plt.xlabel('Number of Followers')
        plt.ylabel('Proportion of Tweets')
        
        plt.xlim(0,self.binSize*self.numberOfBins)
        
        plt.show()
        
    def save(self):
        try:
            with open('data.txt', 'w') as outfile:
                json.dump(self.bins, outfile)
                print('file saved')
        except:
            print("file save error")
        
    def load(self):
        with open('data.txt') as outfile:
            self.bins=json.load(outfile)
            self.binSize=self.bins[0]['numTo']-self.bins[0]['numFrom']
            self.numberOfBins=len(self.bins)
            
    def normalize(self):
        sumOfTweets=0
        for tweetBin in self.bins:
            sumOfTweets=sumOfTweets+tweetBin['numInBin']
       
        for tweetBin in self.bins:
            tweetBin['density']=tweetBin['numInBin']/sumOfTweets
            

        pass    
                    
        