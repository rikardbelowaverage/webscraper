import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot(x, y, twitter_handle):
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    figure = plt.plot(x,y)
    plt.gcf().autofmt_xdate()
    plt.title("{} likes per tweet".format(twitter_handle))
    plt.ylabel("Likes")
    
    return figure