try:
    from scrape import storeScrape
    from scrape import scrape
    from plot_likes_over_time import plot
    from gui import startGui
    import json
    import pandas as pd
    from io import StringIO

except ModuleNotFoundError:
    print('Please download dependencies from requirement.txt')
except Exception as ex:
    print(ex)

if __name__ == '__main__':
    twitter_handle = startGui()
    count = 200
    filepath = r'C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\{handle}.csv'.format(handle=twitter_handle)
    jsonResponse = scrape(twitter_handle, count);
    df = storeScrape(jsonResponse, filepath)
    plot(filepath,twitter_handle)
    
    

   