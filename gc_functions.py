import requests
from bs4 import BeautifulSoup as bs
import re
import json
import numpy as np
import pandas as pd

def scrape_explore_page(pagenumber):
    """Pagenumber must be from 1 to 20. Returns a pandas dataframe"""
    url = 'https://www.ultimate-guitar.com/explore?'
    params = {'order': 'hitstotal_desc',
              'page': pagenumber,
              'type[]':'Chords'}
    response = requests.get(url, params)
    soup = bs(response.content, 'html.parser')
    content = soup.text.strip().split('\n')
    res = []
    for line in content:
        line = re.sub(r'^[^a]*', '',line)
        if line.startswith('age'):
            res.append(line)
    tempstring = res[3]
    tempstring2 = tempstring.replace('age = ', '')
    tempstring3 = tempstring2[:-1]
    myjson = json.loads(tempstring3)
    templist = []
    for item in myjson['data']['data']['tabs']:
        templist.append(item)
    tempdf = pd.DataFrame(templist)
    return tempdf

def build_most_popular():
    frames = []
    for i in range(20):
        tempdf = scrape_explore_page(i+1)
        frames.append(tempdf)
    tempbigtable = pd.concat(frames)
    return tempbigtable
