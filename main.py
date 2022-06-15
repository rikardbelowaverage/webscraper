try:
    from bs4 import BeautifulSoup
    import pandas as pd
    import requests
    import base64
    from selenium import webdriver
    from keys import api_key, api_key_secret, bearer_token
        
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)

if __name__ == "__main__":
    key = '{}:{}'.format(api_key, api_key_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    
    access_token = auth_resp.json()['access_token']
    search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
    }
    
    search_params = {
        'q': 'Zelenskyy',
        'result_type': 'recent',
        'count': 10
    }
    
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    tweet_data = search_resp.json()