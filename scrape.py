try:
    from bs4 import BeautifulSoup
    import pandas as pd
    import requests
    import base64
    from keys import api_key, api_key_secret, bearer_token
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)
    
def create_url(count,user_id):
    return "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}".format(user_id,count)

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r

def get_params():
    return {"tweet.fields": "attachments"}

def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(f"HTTP Response : {response.status_code}")
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def scrape(user_id, count):
    url = create_url(count,user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    return json_response

def storeScrape(jsonResponse, filepath):
    try:
        df = pd.read_csv(filepath, names=('created_at','favorite_count','id', 'retweet_count','text'), header=0)
    except:
        df = pd.DataFrame()
        print('CSV didn\'t exist, created new file to store data')
    keys = {'created_at','favorite_count','id', 'retweet_count','text'}
    for tweet in jsonResponse:
        cleaned_tweet = {key: tweet[key] for key in tweet.keys() & keys}
        if cleaned_tweet not in df.values:
            df = df.append(cleaned_tweet, ignore_index=True, sort=False)
            df = df.reindex(df.columns, axis=1)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df = df.sort_values(by='created_at')
    df.drop_duplicates(subset=['text'],keep='first', inplace=True, ignore_index=True)
    df.to_csv(filepath)
    return df