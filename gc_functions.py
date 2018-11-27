import requests
from bs4 import BeautifulSoup as bs
import re
import json
import numpy as np
import pandas as pd

def scrape_explore_page(pagenumber, category = 'hitstotal_desc'):
    """Pagenumber must be from 1 to 20. Returns a pandas dataframe"""
    url = 'https://www.ultimate-guitar.com/explore?'
    params = {'order': category,
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
        tempdf = scrape_explore_page(i+1, 'hitstotal_desc')
        frames.append(tempdf)
    tempbigtable = pd.concat(frames)
    return tempbigtable

def build_highest_rated():
    frames = []
    for i in range(20):
        tempdf = scrape_explore_page(i+1, 'rating_desc')
        frames.append(tempdf)
    tempbigtable = pd.concat(frames)
    return tempbigtable

def combine_and_remove_duplicates(df1, df2):
    combotable = pd.concat([df1, df2])
    cleancombotable = combotable.drop_duplicates(subset = 'tab_url')
    return cleancombotable

def launch_spotipy():
    """Returns an instance of spotipy"""
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    client_credentials_manager = SpotifyClientCredentials(client_id='ac2725d119934aa8a768254b50954af1', client_secret='42e73e9fc67a4a479b207778eb01d0fc')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp
