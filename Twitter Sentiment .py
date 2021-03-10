import os
import json 
import pandas as pd
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from twython import Twython 
from twython import TwythonStreamer 

api_key = '********'
api_secret = '*********'
access_token =  '*********'
access_token_secret = '***********'

#Instantiate an object
python_tweets = Twython(api_key, api_secret)

#Create query 
query = {'q': 'covid', 'result_type': 'popular', 'count': 100, 'lang': 'en'}
# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)


#More advanced search 
search_terms = '(covid) OR (corona) OR (outbreak) OR (social distancing) OR (wear a mask) OR (wearing a mask) OR (pandemic) OR (epidemic) OR (quarantine) OR (stay at home) OR (stay home) OR (work from home) OR (remote work) OR (vaccine) OR (lockdown) OR (reopen) OR (flatten the curve)'

# Instantiate an object
python_tweets2 = Twython(api_key, api_secret)
        
# Create our query
query = {'q': search_terms,
       # 'result_type': 'popular',
        'count': 1000,
        'lang': 'en',
       # 'until': '2020-07-15'
        }

# Search tweets
dict2_ = {'tweet id': [],'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets2.search(**query)['statuses']:
    dict2_['tweet id'].append(status['id'])
    dict2_['user'].append(status['user']['screen_name'])
    dict2_['date'].append(status['created_at'])
    dict2_['text'].append(status['text'])
    dict2_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict2_)
#print(df['date'].unique())
print(df.shape)
df.head(5)

# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d
    
    
# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):     

    # Received data
    def on_success(self, data):
        try:
            if data['lang'] == "en": #Only collect tweets in English
                tweet_data = process_tweet(data)
                self.save_to_csv(tweet_data)
        except:
            'error - nothing added to csv'

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))
# Instantiate from our streaming class
stream = MyStreamer(api_key, api_secret, 
                   access_token, access_token_secret)

#Specify the words you are interested in
tracking = ['covid', 'corona', 'outbreak', 'social distancing', 'wear a mask', 'wearing a mask', 'pandemic',
           'epidemic', 'outbreak', 'quarantine', 'stay at home', 'work from home', 'remote work', 'vaccine',
           'lockdown', 'reopen', 'flatten the curve', 'stay home']

# Start the stream
stream.statuses.filter(track = tracking)

#Analyze saved tweets
columns = ['Hashtags', 'Text', 'User', 'Location']
tweets = pd.read_csv("saved_tweets.csv", encoding='latin1', names = columns)
tweets.head()

