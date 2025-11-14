## Import Libraries
import warnings
import regex as re

from urllib.parse import unquote, urlencode
import urllib3
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
from urllib.request import urlopen

warnings.filterwarnings('ignore')

import numpy as np
from time import sleep
from random import randint
from selenium import webdriver

quote_page01= 'https://www.drive.com.au/showrooms/mitsubishi/asx/#review/'
quote_page02= 'https://www.drive.com.au/reviews/'

def htmlParser(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    # print(r.__dict__)
    try:
        if r.status == 200:
            page= r.data
            print("Type of the variable 'page':", page.__class__.__name__)
            print(f"Page Retrieved. Request Status: {r.status}, Page Size: {len(page)}")
        else:
            print(f"Some problem occurred. Request Status: {r.status}")
    except Exception as e:
        print(f"Error while processing response: {e}")
    
    soup = BeautifulSoup(page, 'html.parser')
    print('Type of the variable \'soup\':', soup.__class__.__name__)
    return soup

soup01 = htmlParser(quote_page01)

# <div class="articleCard_drive-article-card__thumbnail__description__SMZd8">The latest special-edition Mitsubishi ASX aims to amp up the small SUV's street appeal with a range of black accessories.</div>
# /html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div[2]

results = soup01.find_all("div", class_="articleCard_drive-article-card__thumbnail__description__SMZd8")
# print(results)
reviews = [review.text for review in results]
# reviews = []
# for review in results:
#     reviews.append(review.text)

print(reviews[0:5])

soup02 = htmlParser(quote_page02)
