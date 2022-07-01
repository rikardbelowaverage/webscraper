import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import plot_likes_over_time

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def startGui():    
    layout = [[sg.Text('Enter twitter-handle to scrape')],      
                     [sg.InputText(key='-IN-')],      
                     [sg.Submit(), sg.Cancel()]]      
    
    window = sg.Window('Window Title', layout)    
    
    event, values = window.read()    
    window.close()
    
    twitter_handle = values['-IN-']    
    sg.popup('Scraping data from ', twitter_handle)
    
    return twitter_handle
    
    
    