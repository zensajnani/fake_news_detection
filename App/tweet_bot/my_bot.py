#!/usr/bin/env python
# coding: utf-8

# In[24]:


import tweepy
import time
import joblib

from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

#Twitter Bot


# In[26]:


print("This is my bot!")


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'

pipeline = joblib.load('../pipeline_final.sav')


# In[27]:


#this to reply to tweets only once 
#this is to retrieve the last seen id
def retrieve_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


# In[28]:


#this is to store last seen id/rewrite it 
def store_last_seen_id(last_seen_id, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    
    f_write.close()
    return


# In[29]:


#Detect if tweet is real or fake news
def predict_tweet_news(text):
    pred = pipeline.predict(text)
    return pred


# In[32]:



def reply_to_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # We need to use tweet_mode='extended' to show all full tweets
    
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#news' in mention.full_text.lower():
            print('found #news')
            print('responding back...')
            #this is used to reply to the tweets tagged to us
            tweet_received = [mention.full_text]
            prediction = predict_tweet_news(tweet_received)
            api.update_status(f'#news @{mention.user.screen_name} This is {prediction}!', mention.id)


# In[33]:
reply_to_tweets()
# while True:
#     reply_to_tweets()
#     time.sleep(2)


# In[ ]:




