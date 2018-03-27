


import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "AJTbg1cGiQPb6im9zXc2iAjcq"
consumer_secret = "HhYRyKqtyBGpk0rwlHAtCazxVsth0KU35bKcKGFPIbJwiDP03t"
access_key = "928680513019277317-RodSVJC6BDywnLZBrJujHUZOoZNE1DQ"
access_secret = "6RRlakvsQKqkER0k1MmJ7K0BkjD8nDOQx8BH1SFh2QmkH"
twitter_name = "@realDonaldTrump"


#credit to yanofsky - https://gist.github.com/yanofsky/5436496
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    print "here"
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    #write the csv  
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    return

get_all_tweets(twitter_name)

"""list_of_Tweets = get_all_tweets(twitter_name)

print list_of_Tweets
with open('trumpTweets.txt', 'a') as outFile:
    list_of_Tweets = get_all_tweets(twitter_name)
    for tweet in list_of_Tweets:
        print tweet
        outFile.write(tweet[2])
        outFile.write('/n')"""








