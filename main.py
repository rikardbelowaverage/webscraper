try:
    from bs4 import BeautifulSoup
    import pandas as pd
    import requests
    from selenium import webdriver
        
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)

if __name__ == "__main__":
    # Which twitter user you would like to get data from
    url = 'https://twitter.com/ZelenskyyUa'
    # Send a http request to url
    html_content=requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    data = {}
    tweet_data = soup.find("span", attrs={"class": "css-901oao css"})
    print(tweet_data)