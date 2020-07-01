from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import csv

begin_date = dt.date(2020,6,30)
end_date = dt.date(2020,7,2)

limits = input("Enter number of tweets you want to scrape:\n")
limits = int(limits)

langs = "english"

tweets = query_tweets("news" , begindate=begin_date, enddate=end_date , limit=limits, lang=langs)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv("C:/fake_news_detection/tweet.csv" , index= False)
