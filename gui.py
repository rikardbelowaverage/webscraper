import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import plot_likes_over_time
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from plot_likes_over_time import plot
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
from PIL import Image, ImageQt
import numpy as np
import os
import sys
from scrape import scrape
from scrape import storeScrape


def startGui():    
    layout = [[sg.Text('Enter twitter-handle to scrape')],      
                     [sg.InputText(key='-IN-')],      
                     [sg.Submit(), sg.Cancel()]]      
    
    window = sg.Window('Window Title', layout)    
    event, values = window.read()    
    window.close()
    twitter_handle = values['-IN-']    
    sg.popup('Scraping data from ', twitter_handle)
    viewPlot(twitter_handle)

    return twitter_handle

def getData(twitter_handle): 
    count = 200
    try:
        jsonResponse = scrape(twitter_handle, count);
        filepath = r"C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\{handle}.csv".format(handle=twitter_handle)
        df = storeScrape(jsonResponse, filepath)
        x,y = pd.to_datetime(df['created_at']), df['favorite_count']
        return x,y
    except:
        print("Error retrieving data")
    


def viewPlot(twitter_handle):
    x,y = getData(twitter_handle)
    fig = plot(x,y,twitter_handle)
