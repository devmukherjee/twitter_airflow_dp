# import tweepy
import pandas as pd
import s3fs

import requests
from datetime import datetime

def run_twitter_etl():

    url = "https://twitter-api47.p.rapidapi.com/v2/user/tweets-and-replies"

    querystring = {"userId":"34743251"}

    headers = {
        "x-rapidapi-key": "f7f63e4fb7mshb13f97223b4fd53p13298ajsnf736fd0f8f77",
        "x-rapidapi-host": "twitter-api47.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    json_data= response.json()
    """
    extract tweet id,
    views count, 
    created_at
    fulltext
    """
    tweet_data= map(lambda x: [x['rest_id']\
                            ,int(x['views']['count'])\
                                ,x['legacy']['created_at']\
                                ,x['legacy']['full_text']],\
                                json_data['tweets'])

    tweet_data_df= pd.DataFrame(data= tweet_data,\
                                columns=['tweet_id','view_count','created_at','full_text'])

    # print(tweet_data_df.head(10))

    #Transform
    converter = lambda ts: datetime.strptime(ts, "%a %b %d %H:%M:%S %z %Y")

    tweet_data_df['view_count']= tweet_data_df['view_count'].astype('int')
    tweet_data_df['created_at']= tweet_data_df['created_at'].apply(converter)

    print("\n Minute is :%s \n ",datetime.now().minute)
    tweet_data_df.to_csv(f"s3://dev-twitter-rapidapi-bucket/spacex_tweet_data_{datetime.now().minute}.csv", index= False)

if __name__=='__main__':
    run_twitter_etl()
