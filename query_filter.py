import re 
import tweepy 
from tweepy import OAuthHandler 

class TwitterClient(object): 


    def __init__(self): 
           
           
            consumer_key = 'YEqsXJAuiCQa0k5NJ1HCdExo7'
            consumer_secret = 'n7b0xngiRmU3uXQ6SzoF9dzbNjMWVuS3mK5MVGocimWVgAKbjn'
            access_token = 'AAAAAAAAAAAAAAAAAAAAAAxXLgEAAAAAknuf0ZzNSmHPw87SShNl%2BJul40E%3DiqtxUtAJslHVbmfdj88mAOWmP5T3NEcyUBtIgGQ9BWnglwGRSF'
            #access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
      

            try:  
                self.auth = OAuthHandler(consumer_key, consumer_secret) 
                self.auth.set_access_token(access_token) 
                self.api = tweepy.API(self.auth) 
            except: 
                print("Error: Authentication Failed") 
                

    def get_tweets(self, query, count = 10): 
            ''' 
            Main function to fetch tweets and parse them. 
            '''
            # empty list to store parsed tweets 
            tweets = [] 
            sentiment=utils()
            try: 
                # call twitter api to fetch tweets 
                fetched_tweets = self.api.search(q = query, count = count) 
      
                # parsing tweets one by one 
                for tweet in fetched_tweets: 
                    # empty dictionary to store required params of a tweet 
                    parsed_tweet = {} 
      
                    # saving text of tweet 
                    parsed_tweet['text'] = tweet.text 
                    # saving sentiment of tweet 
                    parsed_tweet['sentiment'] = sentiment.predict_result(tweet.text) 
      
                    # appending parsed tweet to tweets list 
                    if tweet.retweet_count > 0: 
                        # if tweet has retweets, ensure that it is appended only once 
                        if parsed_tweet not in tweets: 
                            tweets.append(parsed_tweet) 
                    else: 
                        tweets.append(parsed_tweet) 
      
                # return parsed tweets 
                return tweets 
      
            except tweepy.TweepError as e: 
                # print error (if any) 
                print("Error : " + str(e)) 
            
            

def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    query1=input("Enter the topic related to which you want sentiment")
    tweets = api.get_tweets(query = query1, count = 200) 
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} % \ ".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))) 
  
    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
  
if __name__ == "__main__": 
    # calling main function 
    main() 