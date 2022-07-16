from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog, QApplication, QPushButton, QVBoxLayout, QLineEdit,QComboBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
import matplotlib.pyplot as plt
from scrape import scrape, storeScrape
import pandas as pd
import os

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Twitter scraper")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.uiComponents()
        
    def uiComponents(self):
        self.button = QPushButton('Scrape data from twitter user')
        self.button.clicked.connect(self.plot)
        self.button.resize(30,20)
        
        self.plotbtn = QPushButton('Plot data from twitter user')
        self.plotbtn.clicked.connect(self.plotDataFromDB)
        
        self.label = QLabel()
        self.label.setText("Available dataframes")
        self.combo = QComboBox()
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
        # adding label to the layout
        layout.addWidget(self.label)
        self.setLayout(layout)
        # adding combobox to the layout
        layout.addWidget(self.combo)
        layout.addWidget(self.plotbtn)
        
        
        self.fillCombo()
    
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
    
    def plotDataFromDB(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        twitter_handle =  self.combo.currentText()
        twitter_handle = os.path.splitext(twitter_handle)[0]
        x,y = getDataFromDB(twitter_handle)
        ax.plot(x,y)
        ax.set_xlabel("Date")
        ax.set_ylabel("Tweets")
        ax.set_title("{} likes per tweet".format(twitter_handle))
        self.canvas.draw()
        
    def fillCombo(self):
        db_path = r"C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe"
        count = 0
        db_names = []
        for path in os.listdir(db_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(db_path, path)):
                count += 1
                db_names.append(path)
        self.combo.addItems(db_names)
        
def getDataFromDB(twitter_handle):
    filepath = r"C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\{handle}.csv".format(handle=twitter_handle)
    df = pd.read_csv(filepath)
    x,y = pd.to_datetime(df['created_at']), df['favorite_count']
    return x,y

def getData(twitter_handle): 
    count = 200
    try:
        jsonResponse = scrape(twitter_handle, count);
        filepath = r"C:\Users\rikar\Documents\Skola\KAU\Projekt\dataframe\{handle}.csv".format(handle=twitter_handle)
        df = storeScrape(jsonResponse, filepath)
        x,y = pd.to_datetime(df['created_at']), df['favorite_count']
        return x,y, twitter_handle
    except:
        print(r"Couldn't retrieve data from twitter user {twitter_handle}")


        
def startGui():
    # creating apyqt5 application
    app = QApplication(sys.argv)
    # creating a window object
    main = Window()
    # showing the window
    main.show()
    # loop
    sys.exit(app.exec_())