import requests
from bs4 import BeautifulSoup as bs
import re
import json
import numpy as np
import pandas as pd
import zipfile
import sys
import requests
import nltk
from nltk.sentiment import SentimentAnalyzer
sa = SentimentAnalyzer()
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
sid = SentimentIntensityAnalyzer()
from selenium.webdriver import Firefox
import random
import time
import warnings
import pymongo
from selenium.common.exceptions import TimeoutException

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

def launch_spotipy(myclientid, myclientsecret):
    """Returns an instance of spotipy"""
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    client_credentials_manager = SpotifyClientCredentials(client_id=myclientid, client_secret=myclientsecret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def print_sentiments(sentences):
    """Given a list of sentences, prints sentiment information"""
    for sentence in sentences:
        print(sentence)
        ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()

def extract_user_comments(allcomments):
    newcommentlist = []
    for i in range(len(allcomments)):
        for j in range(len(allcomments[i])):
            tempcommentlist = []
            tempstring = allcomments[i][j]
            splitstring = tempstring.split('\n',3)
            tempcomment = splitstring[0]
            newsplitstring = splitstring[2].replace('[a]', '')
            newsplitstring2 = newsplitstring.replace('  ', ' ')
            tempuser = newsplitstring2
            tempcommentlist.append(tempuser)
            tempcommentlist.append(tempcomment)
            newcommentlist.append(tempcommentlist)
    return newcommentlist

def get_all_comments(urllist):
    browser = Firefox()
    allcomments = []
    for url in urllist:
        browser.get(url)
        sleep(10,15)
        bottomofpage = browser.find_element_by_css_selector('a._3FEu1 > span:nth-child(1) > span:nth-child(1)')
        bottomofpage.location_once_scrolled_into_view
        sleep(10,15)
        button = browser.find_element_by_css_selector('._39WCv > button:nth-child(1)')
        button.click()
        sleep(10,15)
        rawcomments = browser.find_elements_by_class_name('_300X0')
        comments = []
        for i in range(len(rawcomments)):
            comments.append(rawcomments[i].text)
        allcomments.append(comments)
    return allcomments

def get_tab_idxs(user_ratings_df, item_factors_df):
    tab_idxs = []
    for tab_id in user_ratings_df['tab']:
        tab_idx = item_factors_df.index[item_factors_df['id'] == tab_id]
        tab_idxs.append(tab_idx[0])
    return np.array(tab_idxs)

def new_user_predict(newuser_factors, item_factor_arr):
    new_factor_list = []
    for i in range(len(item_factor_arr)):
        new_factor_list.append(np.dot(newuser_factors, item_factor_arr[i]))
    new_user_df = pd.DataFrame([new_factor_list], index=['newuser'])
    return new_user_df

def check_db_size(mc):
    raw_bunch_list = list(mc['Guitar']['Tabs'].find())
    return len(raw_bunch_list)

def sleep(start=5, end=15):
  return time.sleep(random.randint(5, 15))

def make_url_list(combinedtable):
    sitelist = list(combinedtable['tab_url'])
    songlist = list(combinedtable['song_name'])
    urllist = []
    for i in range(len(sitelist)):
        templist = []
        templist.append(sitelist[i])
        templist.append(songlist[i])
        urllist.append(templist)
    return urllist

def get_data(urls, mc):
    browser = Firefox(timeout = 45)
    for url in urls:
        try:
            commentlist = get_comments(url, mc, browser)
        except TimeoutException as e:
            warnings.warn(f"url: {url}\n{repr(e)}")
            continue
        except Exception as e:
            warnings.warn(f"url: {url}\n{repr(e)}")
            continue
    browser.close()

def get_comments(url, mc, browser):
    commentlist = load_commentlist(url, mc)
    if commentlist is None:
        commentlist = scrape_comments(url, browser)
        store_commentlist(url,commentlist, mc)
    return commentlist

def load_commentlist(url, mc):
    result = mc['Guitar']['Tabs'].find_one({'url':url[0]})
    if result:
        return result['commentlist']

def store_commentlist(url, commentlist, mc):
    mc['Guitar']['Tabs'].delete_many({'url':url})
    mc['Guitar']['Tabs'].insert_one({'commentlist':commentlist,'url':url})

def scrape_comments(url, browser):
    browser.get(url[0])
    sleep(5,10)
    bottomofpage = browser.find_element_by_css_selector('a._3FEu1 > span:nth-child(1) > span:nth-child(1)')
    bottomofpage.location_once_scrolled_into_view
    sleep(5,10)
    button = browser.find_element_by_css_selector('._39WCv > button:nth-child(1)')
    button.click()
    sleep(10,15)
    rawcomments = browser.find_elements_by_class_name('_300X0')
    comments = []
    for j in range(len(rawcomments)):
        comments.append([rawcomments[j].text, url[1]])
    return comments

def get_keys():
    with open('mongokey.txt', 'r') as myfile:
        mongostring = myfile.read().replace('\n', '')
    with open('spotifyclientid.txt', 'r') as myfile2:
        myclientid = myfile2.read().replace('\n', '')
    with open('spotifyclientsecret.txt', 'r') as myfile3:
        myclientsecret = myfile3.read().replace('\n', '')
    return mongostring, myclientid, myclientsecret
