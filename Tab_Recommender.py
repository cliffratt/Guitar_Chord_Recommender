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
from random import randint
import time
import warnings
import pymongo
import pickle
from random import shuffle
from functools import reduce
from selenium.common.exceptions import TimeoutException
from pyspark.ml.recommendation import ALS, ALSModel
from pyspark.ml.tuning import CrossValidator
from pyspark.sql.types import (
    IntegerType, StringType, IntegerType, FloatType,
    StructField, StructType, DoubleType)
from gc_functions import (get_keys, launch_spotipy, scrape_explore_page, build_most_popular,
                          build_highest_rated, combine_and_remove_duplicates, print_sentiments,
                          extract_user_comments, get_tab_idxs, new_user_predict,
                          check_db_size, sleep, make_url_list, get_data, get_comments, load_commentlist,
                          store_commentlist, scrape_comments, download_mongodb, assign_id_numbers)

def cls(num=100):
    print("\n" * 100)

#def unpickling():
#

def welcome_screen():
    print("=============================================================================                                                                  ")
    print("=============================================================================                                                                  ")
    print("===   _____       _ _               _______    _                          ===                        q o o p                                   ")
    print("===  / ____|     (_) |             |__   __|  | |                         ===                        q o!o p                                   ")
    print("=== | |  __ _   _ _| |_ __ _ _ __     | | __ _| |__                       ===                        d o!o b                                   ")
    print("=== | | |_ | | | | | __/ _` | '__|    | |/ _` | '_ \                      ===                         \!!!/                                    ")
    print("=== | |__| | |_| | | || (_| | |       | | (_| | |_) |                     ===                         |===|                                    ")
    print("===  \_____|\__,_|_|\__\__,_|_|       |_|\__,_|_.__/                      ===                         |!!!|                                    ")
    print("===                                                                       ===                         |!!!|                                    ")
    print("===  _____                                                   _            ===                         |!!!|                                    ")
    print("=== |  __ \                                                 | |           ===                         |!!!|                                    ")
    print("=== | |__) |___  ___ ___  _ __ ___  _ __ ___   ___ _ __   __| | ___ _ __  ===                         |!!!|                                    ")
    print("=== |  _  // _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _ \ '__| ===                        _|!!!|__                                  ")
    print("=== | | \ \  __/ (_| (_) | | | | | | | | | | |  __/ | | | (_| |  __/ |    ===                      .+=|!!!|--.`.                               ")
    print("=== |_|  \_\___|\___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__,_|\___|_|    ===                    .'   |!!!|   `.\                              ")
    print("=============================================================================                   /     !===!     \\                             ")
    print("============================= Version 1.0 ===================================                   |    /|!!!|\    ||                             ")
    print("=============================================================================                    \   \!!!!!/   //                              ")
    print("                                                                                                  )   `==='   ((                               ")
    print("                                                                                                .'    !!!!!    `..                             ")
    print("                                                                                               /      !!!!!      \\                            ")
    print("                                                                                              |       !!!!!       ||                           ")
    print("                                                                                              |       !!!!!       ||                           ")
    print("                                  By:                                                         |       !!!!!       ||                           ")
    print("                             Ryan Ratcliffe                                                    \     =======     //                            ")
    print("                                                                                                `.    ooooo    .;'                             ")
    print("                                                                                                  `-._______.-'                                ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("__        ___           _   _                                                                           ")
    print("\ \      / / |__   __ _| |_(_)___ _   _  ___  _   _ _ __ _ __   __ _ _ __ ___   ___                     ")
    print(" \ \ /\ / /| '_ \ / _` | __| / __| | | |/ _ \| | | | '__| '_ \ / _` | '_ ` _ \ / _ \                    ")
    print("  \ V  V / | | | | (_| | |_| \__ \ |_| | (_) | |_| | |  | | | | (_| | | | | | |  __/                    ")
    print("   \_/\_/  |_| |_|\__,_|\__|_|___/\__, |\___/ \__,_|_|  |_| |_|\__,_|_| |_| |_|\___|                    ")
    print("                                  |___/                                                                 ")
    name = input("Your Name ==>  ")
    #print("Your name is: ", name)
    return name

def selection_screen(name):
    cls()
    print("===================================================")
    print("===================================================")
    print("===   _____      _           _   _              ===")
    print("===  / ____|    | |         | | (_)             ===")
    print("=== | (___   ___| | ___  ___| |_ _  ___  ___    ===")
    print("===  \___ \ / _ \ |/ _ \/ __| __| |/ _ \| '_ \  ===")
    print("===  ____) |  __/ |  __/ (__| |_| | (_) | | | | ===")
    print("=== |_____/ \___|_|\___|\___|\__|_|\___/|_| |_| ===")
    print("===================================================")
    print("===================================================")
    print('                         ')
    print('1. Find Guitar Tabs      ')
    print('2. Display Random Tab    ')
    print('3. Show Top Genres       ')
    print('                         ')
    print('0. Exit                  ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    print('                         ')
    selection = input(f"Hello {name}. What is your selection? ==>  ")
    return selection

def survey_screen(name):
    usergenrepicks = []
    with open('data/top63genres.pkl', 'rb') as handle:
        top63genres = pickle.load(handle)
    selection = ""
    templength = len(top63genres)
    while (selection!= '0' and selection!= '111'):
        cls()
        print("=========================================")
        print("=========================================")
        print("===   _____                           ===")
        print("===  / ____|                          ===")
        print("=== | |  __  ___ _ __  _ __ ___  ___  ===")
        print("=== | | |_ |/ _ \ '_ \| '__/ _ \/ __| ===")
        print("=== | |__| |  __/ | | | | |  __/\__ \ ===")
        print("===  \_____|\___|_| |_|_|  \___||___/ ===")
        print("=========================================")
        print("=========================================")
        print("Genres left: " + str(len(top63genres)))
        print('Enter the number of a genre that you like:')
        print('                         ')
        tempnum = 20
        if len(top63genres) < tempnum:
            tempnum = len(top63genres)
        for i in range(tempnum):
            print(str(i+1) + ': ' + str(top63genres[i]))
        for j in range (20-tempnum):
            print("")
        print('                         ')
        print('111. Done Picking          ')
        print('222. Give More Genre Choices')
        print('0. Back to selection screen')
        print('                         ')
        print('                         ')
        print('                         ')
        if(len(usergenrepicks)>0):
            tempstring = "Your Picks: " + str(usergenrepicks[0])
            for i in range(len(usergenrepicks)-1):
                tempstring += " , " + str(usergenrepicks[i+1])
            print(tempstring)
        else:
            print("Your Picks: ")
        print('                         ')
        selection = input(f"Hello {name}. What is your selection? ==>  ")
        if(selection == '222'):
            tempnum = 20
            if templength > 20:
                for i in range(20):
                    del top63genres[0]
                    templength -= 1
        if(selection!= '0' and selection!= '111' and selection!='222'):
            usergenrepicks.append(top63genres[int(selection)-1])
            if(templength > 1):
                del top63genres[int(selection)-1]
                templength -=1
            else:
                selection = '111'
        if(selection == '111'):
            pick_songs_you_like(name, usergenrepicks)
    return selection

def pick_songs_you_like(name, usergenrepicks):
    selection = ""
    itemidxs = []
    usersongpicks = []
    combinedtable = pd.read_pickle('data/combinedtable.pkl')
    possiblesongs = []
    i = 0
    for item in combinedtable['genre']:
        for subitem in item:
            if subitem in usergenrepicks:
                if combinedtable['song_name'].iloc[i] not in possiblesongs:
                    possiblesongs.append(combinedtable['song_name'].iloc[i])
                    itemidxs.append(i)
        i += 1
    shuffle(possiblesongs)
    while (selection!= '0' and selection!= '111'):
        cls()
        print("=====================================================================================================")
        print("=====================================================================================================")
        print("===    _____                    __     __         _      _ _     _______    _____  _              ===")
        print("===   / ____|                   \ \   / /        | |    (_) |   |__   __|  |  __ \| |             ===")
        print("===  | (___   ___  _ __   __ _ __\ \_/ /__  _   _| |     _| | _____| | ___ | |__) | | __ _ _   _  ===")
        print("===   \___ \ / _ \| '_ \ / _` / __\   / _ \| | | | |    | | |/ / _ \ |/ _ \|  ___/| |/ _` | | | | ===")
        print("===   ____) | (_) | | | | (_| \__ \| | (_) | |_| | |____| |   <  __/ | (_) | |    | | (_| | |_| | ===")
        print("===  |_____/ \___/|_| |_|\__, |___/|_|\___/ \__,_|______|_|_|\_\___|_|\___/|_|    |_|\__,_|\__, | ===")
        print("===                       __/ |                                                             __/ | ===")
        print("===                      |___/                                                             |___/  ===")
        print("=====================================================================================================")
        print("=====================================================================================================")
        print("Songs left: " + str(len(possiblesongs)))
        print('Enter the number of a song that you like to play on the guitar')
        print('                         ')
        tempnum = 20
        if len(possiblesongs) < tempnum:
            tempnum = len(possiblesongs)
        for i in range(tempnum):
            print(str(i+1) + ': ' + str(possiblesongs[i]))
        for j in range (20-tempnum):
            print("")
        print('                         ')
        print('111. Give Recommendations Now ')
        print('222. Show More Songs  ')
        print('0. Back to selection screen')
        print('                         ')
        print('                         ')
        if(len(usersongpicks)>0):
            tempstring = "Your Picks: " + str(usersongpicks[0])
            for i in range(len(usersongpicks)-1):
                tempstring += " , " + str(usersongpicks[i+1])
            print(tempstring)
        else:
            print("Your Picks: ")
        print('                         ')
        selection = input(f"Hello {name}. What is your selection? ==>  ")
        if(selection == '222'):
            tempnum = 20
            if len(possiblesongs) > 20:
                for i in range(20):
                    del possiblesongs[0]
        if(selection!= '0' and selection!= '111' and selection != '222'):
            usersongpicks.append(possiblesongs[int(selection)-1])
            del possiblesongs[int(selection)-1]
        if(selection == '111'):
            recommendations_page(name, usersongpicks, itemidxs)
    return selection

def recommendations_page(name, usersongpicks, itemidxs):
    combinedtable = pd.read_pickle('data/combinedtable.pkl')
    recommendations = []
    item_factors_df2 = pd.read_pickle('data/item_factors_df2.pkl')
    item_factors_arr = np.array(item_factors_df2['features'].tolist())
    selection = ""
    tabidxs = np.array(itemidxs)
    ratingslist = []
    for i in range(len(itemidxs)):
        ratingslist.append([.9500])
    ratings = np.array(ratingslist)
    X, residuals, rank, s = np.linalg.lstsq(item_factors_arr[tabidxs], ratings, rcond=None)
    newuser_factors = X
    new_factor_list = []
    for i in range(len(item_factors_arr)):
        new_factor_list.append([np.dot(newuser_factors.T, item_factors_arr[i].reshape(-1,1)), i])
    recommendations = sorted(new_factor_list, key=lambda x: x[0])[-100:][::-1]
    shuffle(recommendations)
    while (selection!= '0'):
        cls()
        print('=================================================================================================')
        print('=================================================================================================')
        print("===  _____                                                    _       _   _                   ===")
        print("===  |  __ \                                                 | |     | | (_)                  ===")
        print("===  | |__) |___  ___ ___  _ __ ___  _ __ ___   ___ _ __   __| | __ _| |_ _  ___  _ __  ___   ===")
        print("===  |  _  // _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _` | __| |/ _ \| '_ \/ __|  ===")
        print("===  | | \ \  __/ (_| (_) | | | | | | | | | | |  __/ | | | (_| | (_| | |_| | (_) | | | \__ \  ===")
        print("===  |_|  \_\___|\___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__,_|\__,_|\__|_|\___/|_| |_|___/  ===")
        print('=================================================================================================')
        print('=================================================================================================')
        print("Recommendations left: " + str(len(recommendations)))
        print("")
        for i in range(20):
            print(str(i+1) + ": " + str(combinedtable['song_name'].iloc[(int(recommendations[i][1]))]) + " by " + str(combinedtable['artist_name'].iloc[(int(recommendations[i][1]))]))
        print()
        print()
        print()
        print()
        print()
        print()
        print('1 - 20. Get Information For Song In List')
        print('111. Get More Recommendations')
        print('0. Back to selection screen')
        print('                         ')
        selection = input(f"Hello {name}. What is your selection? ==>  ")
        if (int(selection) >= 1 and int(selection) <= 20):
            display_tab_info(name, selection, recommendations)
        if(selection == '111'):
            if len(recommendations) > 20:
                for i in range(20):
                    del recommendations[0]
    return selection

def display_tab_info(name, choice, recommendations):
    combinedtable = pd.read_pickle('data/combinedtable.pkl')
    selection = ""
    myint = int(choice)
    while selection!= '0':
        cls()
        print("=======================================================================================")
        print("=======================================================================================")
        print("===   _______    _    _____        __                           _   _               ===")
        print("===  |__   __|  | |  |_   _|      / _|                         | | (_)              ===")
        print("===     | | __ _| |__  | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __    ===")
        print("===     | |/ _` | '_ \ | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \   ===")
        print("===     | | (_| | |_) || |_| | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | |  ===")
        print("===     |_|\__,_|_.__/_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|  ===")
        print("=======================================================================================")
        print("=======================================================================================")
        print()
        print()
        print()
        print('Song Name: ' + str(combinedtable['song_name'].iloc[(int(recommendations[myint-1][1]))]))
        print('Artist Name: ' + str(combinedtable['artist_name'].iloc[(int(recommendations[myint-1][1]))]))
        print('Genres: ' + str(combinedtable['genre'].iloc[(int(recommendations[myint-1][1]))]))
        print()
        print('Tab URL: ' + str(combinedtable['tab_url'].iloc[(int(recommendations[myint-1][1]))]))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('111. Open Tab URL in a Firefox Browser')
        print('0. Back To Recommendations Page')
        print()
        selection = input(f"Hello {name}. What is your selection? ==>  ")
        if (selection == '111'):
            browser = Firefox(timeout = 45)
            browser.get(str(combinedtable['tab_url'].iloc[(int(recommendations[myint-1][1]))]))
    return selection

def display_random(name):
    combinedtable = pd.read_pickle('data/combinedtable.pkl')
    selection = ""
    while selection!= '0':
        myint = randint(0, 932)
        cls()
        print("==========================================================================")
        print("==========================================================================")
        print("===  _____                 _                  _____                    ===")
        print("=== |  __ \               | |                / ____|                   ===")
        print("=== | |__) |__ _ _ __   __| | ___  _ __ ___ | (___   ___  _ __   __ _  ===")
        print("=== |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \ \___ \ / _ \| '_ \ / _` | ===")
        print("=== | | \ \ (_| | | | | (_| | (_) | | | | | |____) | (_) | | | | (_| | ===")
        print("=== |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|_____/ \___/|_| |_|\__, | ===")
        print("===                                                              __/ | ===")
        print("===                                                             |___/  ===")
        print("==========================================================================")
        print("==========================================================================")
        print('                         ')
        print('1. Get another random song')
        print('0. Back to selection screen')
        print('                         ')
        print('Song Name: ' + str(combinedtable['song_name'].iloc[myint]))
        print('Artist Name: ' + str(combinedtable['artist_name'].iloc[myint]))
        print('Genres: ' + str(combinedtable['genre'].iloc[myint]))
        print('                         ')
        print('Tab URL: ' + str(combinedtable['tab_url'].iloc[myint]))
        print('                         ')
        print('                         ')
        print('                         ')
        print('                         ')
        print('                         ')
        print('                         ')
        print('                         ')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        selection = input(f"Hello {name}. What is your selection? ==>  ")
    return selection

def showtop10(name):
    combinedtable = pd.read_pickle('data/combinedtable.pkl')
    with open('data/top63genres.pkl', 'rb') as handle:
        top63genres = pickle.load(handle)
    cls()
    print("=========================================")
    print("=========================================")
    print("===   _____                           ===")
    print("===  / ____|                          ===")
    print("=== | |  __  ___ _ __  _ __ ___  ___  ===")
    print("=== | | |_ |/ _ \ '_ \| '__/ _ \/ __| ===")
    print("=== | |__| |  __/ | | | | |  __/\__ \ ===")
    print("===  \_____|\___|_| |_|_|  \___||___/ ===")
    print("=========================================")
    print("==================Top20==================")
    print("=========================================")
    for i in range(20):
        print(str(i+1) + ': ' + str(top63genres[i]))
    print()
    print()
    print()
    print()
    print()
    print()
    print('                         ')
    print('                         ')
    print('0. Back to selection screen')
    print('                         ')
    print('                         ')
    selection = input(f"Hello {name}. What is your selection? ==>  ")
    return selection

def mymain():
    name = welcome_screen()
    selection = 100
    while selection != '0':
        selection = selection_screen(name)
        if selection == '1':
            survey_screen(name)
        if selection == '2':
            display_random(name)
        if selection == '3':
            showtop10(name)
    cls(10)

mymain()
