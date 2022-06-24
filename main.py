try:
    from scrape import storeScrape
    from scrape import scrape
    import json
    import pandas as pd
    from io import StringIO
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from datetime import datetime

except ModuleNotFoundError:
    print('Please download dependencies from requirement.txt')
except Exception as ex:
    print(ex)



if __name__ == '__main__':
    twitter_handle = 'ZelenskyyUa';
    count = 200;
    jsonResponse = scrape(twitter_handle, count);
    df = storeScrape(jsonResponse)
    df.head()
    filepath = r'C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\df.csv'
    df = pd.read_csv(filepath, names=('created_at','favorite_count','id', 'retweet_count','text'), header=0)    
    
    df_created_at,df_favourite_count = pd.to_datetime(df['created_at']), df['favorite_count']

    df.info()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    plt.plot(df_created_at,df_favourite_count)
    plt.gcf().autofmt_xdate()
   