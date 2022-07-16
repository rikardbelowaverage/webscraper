# Python Twitter webscraper
#### By Rikard Johansson
###### Tags: `Scrape, data analysis, python`


## :memo: Summarized Project Overview
This project was created as a part of applied programming DVGB06 at Karlstad University.
The objective of the course is to go from an idea to a complete project. For this project I chose to build a twitter scraper.

## :bulb: Why This Project
The main purpose of this project is to apply earlier programming knowledge to create a working product.
I have an interest in data analysis and its opportunities. Therefore I decided to build a webscraper which will force me to create a couple of functionalities.
## :Functionalities:
1. Scrape functionality: the data needs to be generated from somewhere.
2. Transformations: Scraped raw data is inappropriate for rest of operation, therefore it needs to be transformed.
3. Cleaning: Fixing incorrect, incomplete, duplicate or otherwise erroneous data in a data set.
4. Storage: Data needs to be stored prior to continuing the work.
5. Data visualization: The main goal of data visualization is to make it easier to identify patterns, trends and outliers in large data sets.
6. Graphical User Interface(GUI): For ease of use it should be possible to interact using a GUI.

### Steps:
1. User inputs a twitter handle.
2. url is generated.
3. HTTP request made to the generated url
4. The data from the request is looped through and stored in a pandas dataframe.
5. User can see a plot of likes over time for the chosen twitter handle.
