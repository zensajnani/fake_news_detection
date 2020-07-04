import tweepy
import time

print("This is my bot!")

CONSUMER_KEY = 'YSyDCRJID0Cj9wGjjCUvkgTAc'
CONSUMER_SECRET = 'YH6TOJIGRD81TzOkYXIZzG5wL0NRhHcqAvobL4bc27twfbJPdl'
ACCESS_KEY = '1252588880596893696-2ockVNpr0iOA563EOyzPNlEvTStxGo'
ACCESS_SECRET = 'J1ZDodrTNPMkAdkBIPUq2dcFzLs67TwoHnpxXQAsfsZP2'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = 'last_seen_id.txt'

#this to reply to tweets only once 
#this is to retrieve the last seen id
def retrieve_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

#this is to store last seen id/rewrite it 
def store_last_seen_id(last_seen_id, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

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
            api.update_status('@' + mention.user.screen_name +
                    '#news This could be a fake or a real news!', mention.id)
    return mentions

def get_tweet_text(mentions):
    return mentions

while True:
    reply_to_tweets()
    time.sleep(2)
