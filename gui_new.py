from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
import matplotlib.pyplot as plt
from scrape import scrape, storeScrape
import pandas as pd

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Scrape')
        self.button.clicked.connect(self.plot)
        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)
        # creating a Vertical Box layout
        layout = QVBoxLayout()
        # adding tool bar to the layout
        layout.addWidget(self.toolbar)
        # adding canvas to the layout
        layout.addWidget(self.canvas)
        # adding push button to the layout
        layout.addWidget(self.button)
        # setting layout to the main window
        layout.addWidget(self.line)
        self.setLayout(layout)
    
    # action called by the push button
    def plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x,y, twitter_handle = getData(self.line.text())
        ax.plot(x,y)
        ax.set_xlabel("Date")
        ax.set_ylabel("Tweets")
        ax.set_title("{} likes per tweet".format(twitter_handle))
        # refresh canvas
        self.canvas.draw()

def getData(twitter_handle): 
    count = 200
    try:
        jsonResponse = scrape(twitter_handle, count);
        filepath = r"C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\{handle}.csv".format(handle=twitter_handle)
        df = storeScrape(jsonResponse, filepath)
        x,y = pd.to_datetime(df['created_at']), df['favorite_count']
        return x,y, twitter_handle
    except:
        print("Error retrieving data1")
            
        
#if __name__ == '__main__':
def startGui():
    # creating apyqt5 application
    app = QApplication(sys.argv)
    # creating a window object
    main = Window()
    # showing the window
    main.show()
    # loop
    sys.exit(app.exec_())

