try:
    from scrape import scrape
    import json
    import pandas as pd
    from io import StringIO
    import matplotlib as plt

    
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)

def storeScrape(jsonResponse):
    filepath = r'C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\df.csv'
    try:
        df = pd.read_csv(filepath, names=('created_at','id','favorite_count', 'retweet_count','text'), header=0)
    except:
        df = pd.DataFrame()
        print("CSV didn't exist, created new file to store data")
    
    keys = {'created_at','id','favorite_count', 'retweet_count','text'}
    for tweet in jsonResponse:
        cleaned_tweet = {key: tweet[key] for key in tweet.keys() & keys}
        df = df.append(cleaned_tweet, ignore_index=True, sort=False)
        df = df.reindex(df.columns, axis=1)
    df.to_csv(r'C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\df.csv')
    
    return df

if __name__ == "__main__":
    #twitter_handle = "ZelenskyyUa";
    #count = 200;
    #jsonResponse = scrape(twitter_handle, count);
    #df = storeScrape(jsonResponse)
    #df.head()
    filepath = r'C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\df.csv'
    df = pd.read_csv(filepath, names=('created_at','id','favorite_count', 'retweet_count','text'), header=0)
    df.plot(kind='scatter',x='created_at',y='favorite_count',color='red')
    plt.show()
    

