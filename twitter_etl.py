import snscrape.modules.twitter as sntwitter
import json
import pandas as pd
from datetime import datetime
import s3fs


def run_twitter_etl():
    # Creating list to append tweet data to
    attributes_container = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('layoff since:2023-01-01 until:2023-03-13').get_items()):
        if i>999:
            break
        attributes_container.append([tweet.user.username, tweet.date, tweet.likeCount, tweet.sourceLabel, tweet.rawContent])
        
    # Creating a dataframe to load the list
    tweets_df = pd.DataFrame(attributes_container, columns=["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"])

    # Savind the dataframe as CSV file
    tweets_df.to_csv("s3://twitter-bucket-jahnavi/Twitter_data.csv")
