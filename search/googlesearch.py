#importing the libraries we will need
import pandas as pd
import numpy as np
import urllib
from fake_useragent import UserAgent
import requests
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


from selenium import webdriver
import pandas as pd

def google_results(keyword, n_results):
    query = keyword
    query = urllib.parse.quote_plus(query) # Format into URL encoding
    number_result = n_results
    ua = UserAgent()
    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result if "url" in str(i)]
    links=[i.group(1) for i in results if i != None]
    return (links)



def open_results(links):
    #path with chromedriver
    #driver = webdriver.Chrome('/Users/rodrigodutra/Downloads/chromedriver')

    for link in links:
        driver = webdriver.Chrome('/Users/rodrigodutra/Downloads/chromedriver')
        driver.get(link)



keywords = input("insert the keywords: ")

n_results = int(input("Number of results: "))


links = google_results(keywords, n_results)

print(links)

open_results(links)




