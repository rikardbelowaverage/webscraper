try:
    from scrape import storeScrape
    from scrape import scrape
    from gui import startGui
    import json
    import pandas as pd
    from io import StringIO

except ModuleNotFoundError:
    print('Please download dependencies from requirement.txt')
except Exception as ex:
    print(ex)

if __name__ == '__main__':
    startGui()
    #print("test")
    #twitter_handle, filepath = startGui()
    #count = 200
    #jsonResponse = scrape(twitter_handle, count)
    #df = storeScrape(jsonResponse, filepath)
    #plot(filepath,twitter_handle)
    

    
    #filepath = r'C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\{handle}.csv'.format(handle=twitter_handle.lower())
    #jsonResponse = scrape(twitter_handle, count);
    #df = storeScrape(jsonResponse, filepath)
    
