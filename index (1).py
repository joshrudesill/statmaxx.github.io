#Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Beautiful Soup
from bs4 import BeautifulSoup

#Python Libraries
import time
import json
import io
import os.path
import sys
from datetime import datetime


import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize,sent_tokenize

import pandas as pd
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
save_path = "/Users/joshrudesill/Desktop/indextest"

fn = os.path.join (save_path, "Database.txt")


sys.path.append("/Users/joshrudesill/Desktop/indextest")

URLS = ['https://stocktwits.com/symbol/TSLA',
        'https://stocktwits.com/symbol/XSPA',
        'https://stocktwits.com/symbol/FB',
        'https://stocktwits.com/symbol/AMZN',
        'https://stocktwits.com/symbol/NFLX',
        'https://stocktwits.com/symbol/AAPL',
        'https://stocktwits.com/symbol/BABA',
        'https://stocktwits.com/symbol/IMUX',
        'https://stocktwits.com/symbol/CODX',
        'https://stocktwits.com/symbol/YHOO',
        'https://stocktwits.com/symbol/SPY',
        'https://stocktwits.com/symbol/QQQ',
        'https://stocktwits.com/symbol/PENN',
        'https://stocktwits.com/symbol/ACB',
        'https://stocktwits.com/symbol/TTWO',
        'https://stocktwits.com/symbol/SNAP',
        'https://stocktwits.com/symbol/SHIP',
        'https://stocktwits.com/symbol/MVIS',
        'https://stocktwits.com/symbol/KTOV',
        'https://stocktwits.com/symbol/TLRY',
        'https://stocktwits.com/symbol/NVDA',
        'https://stocktwits.com/symbol/SURF',
        'https://stocktwits.com/symbol/AQST',
        'https://stocktwits.com/symbol/SPLK',
        'https://stocktwits.com/symbol/LULU',
        'https://stocktwits.com/symbol/CRON',
        'https://stocktwits.com/symbol/AMRN',
        'https://stocktwits.com/symbol/F',
        'https://stocktwits.com/symbol/DIS',
        'https://stocktwits.com/symbol/GPRO',
        'https://stocktwits.com/symbol/DAL',
        'https://stocktwits.com/symbol/MSFT',
        'https://stocktwits.com/symbol/RCL',
        'https://stocktwits.com/symbol/KO',
        'https://stocktwits.com/symbol/UCO',
        'https://stocktwits.com/symbol/AMC',
        'https://stocktwits.com/symbol/SPCE',
        'https://stocktwits.com/symbol/GILD',
        'https://stocktwits.com/symbol/LYFT',
        'https://stocktwits.com/symbol/UBER',
        'https://stocktwits.com/symbol/SIRI',
        'https://stocktwits.com/symbol/SQ',
        'https://stocktwits.com/symbol/BYND',
        'https://stocktwits.com/symbol/V',
        'https://stocktwits.com/symbol/OXY',
        'https://stocktwits.com/symbol/ET',
        'https://stocktwits.com/symbol/JPM',
        'https://stocktwits.com/symbol/CRBP',
        'https://stocktwits.com/symbol/PLAY',
        'https://stocktwits.com/symbol/ZM',
        'https://stocktwits.com/symbol/ERI',
        'https://stocktwits.com/symbol/CSCO',
        'https://stocktwits.com/symbol/AUY',
        'https://stocktwits.com/symbol/GDM',
        'https://stocktwits.com/symbol/MGM',
        'https://stocktwits.com/symbol/CGC',
        'https://stocktwits.com/symbol/AZN',
        'https://stocktwits.com/symbol/MMM',
        'https://stocktwits.com/symbol/LTRPA',
        'https://stocktwits.com/symbol/CCL',
        'https://stocktwits.com/symbol/EXPE',
        'https://stocktwits.com/symbol/SAVE',
        'https://stocktwits.com/symbol/USO',
        'https://stocktwits.com/symbol/ABT',
        'https://stocktwits.com/symbol/BA',
        'https://stocktwits.com/symbol/TRN',
        'https://stocktwits.com/symbol/TRNX',
        'https://stocktwits.com/symbol/INO',
        'https://stocktwits.com/symbol/BBBY',
        'https://stocktwits.com/symbol/SONO',
        'https://stocktwits.com/symbol/GE',
        'https://stocktwits.com/symbol/AAL',
        'https://stocktwits.com/symbol/FIT',
        'https://stocktwits.com/symbol/BAC',
        'https://stocktwits.com/symbol/NCLH',
        'https://stocktwits.com/symbol/PLUG',
        'https://stocktwits.com/symbol/UAL',
        'https://stocktwits.com/symbol/AMD',
        'https://stocktwits.com/symbol/TWTR',
        'https://stocktwits.com/symbol/GRPN',
        'https://stocktwits.com/symbol/SBUX',
        'https://stocktwits.com/symbol/MRNA',
        'https://stocktwits.com/symbol/MRO',
        'https://stocktwits.com/symbol/ZNGA',
        'https://stocktwits.com/symbol/T',
        'https://stocktwits.com/symbol/APHA',
        'https://stocktwits.com/symbol/LUV',
        'https://stocktwits.com/symbol/XOM',
        'https://stocktwits.com/symbol/JBLU',
        'https://stocktwits.com/symbol/MFA',
        'https://stocktwits.com/symbol/GM',
        'https://stocktwits.com/symbol/NIO',
        'https://stocktwits.com/symbol/NRZ',
        'https://stocktwits.com/symbol/VOO',
        'https://stocktwits.com/symbol/NOK',
        'https://stocktwits.com/symbol/GUSH',
        'https://stocktwits.com/symbol/NKE',
        'https://stocktwits.com/symbol/PFE',
        'https://stocktwits.com/symbol/KOS',
        'https://stocktwits.com/symbol/WFC',
        'https://stocktwits.com/symbol/GOOGL',
        'https://stocktwits.com/symbol/BNGO',
        'https://stocktwits.com/symbol/DELL',
        'https://stocktwits.com/symbol/VTI',
        'https://stocktwits.com/symbol/EVFM',
        'https://stocktwits.com/symbol/EDU',
        'https://stocktwits.com/symbol/AMSC',
        'https://stocktwits.com/symbol/COST',
        'https://stocktwits.com/symbol/IOVA',
        'https://stocktwits.com/symbol/RPAY',
        'https://stocktwits.com/symbol/PUMP',
        'https://stocktwits.com/symbol/MNLO',
        'https://stocktwits.com/symbol/CRWD',
        'https://stocktwits.com/symbol/WDAY',
        'https://stocktwits.com/symbol/BOX',
        'https://stocktwits.com/symbol/CRM',
        'https://stocktwits.com/symbol/Z',
        'https://stocktwits.com/symbol/OKTA',
        'https://stocktwits.com/symbol/HPQ',
        'https://stocktwits.com/symbol/GOOG',
        'https://stocktwits.com/symbol/DKNG',
        'https://stocktwits.com/symbol/HEBT',
        'https://stocktwits.com/symbol/ARCT',
        'https://stocktwits.com/symbol/PRTS',
        'https://stocktwits.com/symbol/ELA',
        'https://stocktwits.com/symbol/APLT',
        'https://stocktwits.com/symbol/RVP',
        'https://stocktwits.com/symbol/NG',
        'https://stocktwits.com/symbol/SILV',
        'https://stocktwits.com/symbol/DXCM',
        'https://stocktwits.com/symbol/COF',
        'https://stocktwits.com/symbol/WES',
        'https://stocktwits.com/symbol/MCD',
        'https://stocktwits.com/symbol/GLD',
        'https://stocktwits.com/symbol/JNUG',
        'https://stocktwits.com/symbol/TVIX',
        'https://stocktwits.com/symbol/UVXY',
        'https://stocktwits.com/symbol/VXX',
        'https://stocktwits.com/symbol/ATOM',
        'https://stocktwits.com/symbol/SAVA',
        'https://stocktwits.com/symbol/SHOP',
        'https://stocktwits.com/symbol/STMP',
        'https://stocktwits.com/symbol/COE',
        'https://stocktwits.com/symbol/KPTI',
        'https://stocktwits.com/symbol/DIA',
        'https://stocktwits.com/symbol/NEM',
        'https://stocktwits.com/symbol/NOW',
        'https://stocktwits.com/symbol/MKTX',
        'https://stocktwits.com/symbol/XRX',
        'https://stocktwits.com/symbol/NLOK',
        'https://stocktwits.com/symbol/STX',
        'https://stocktwits.com/symbol/INVVY',
        'https://stocktwits.com/symbol/ABUS',



        ]



PATH = "/Users/joshrudesill/Downloads/chromedriver"
options = Options()
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
options.add_argument("--no-sandbox")
#options.add_argument("headless")
options.add_argument("blink-settings=imagesEnabled=false")
options.add_argument('no-proxy-server')
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
driver = webdriver.Chrome(PATH, options= options)
now = datetime.now()
timeStart = now.strftime("%H:%M:%S")

for url in URLS:
    print(url[30:])
    driver.get(url)
    element = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'st_3SL2gug'), ""))
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    mentions = soup.findAll(True, {"class": ["st_3SL2gug"]})
    divtime = soup.findAll(True, {"class":"st_28bQfzV st_1E79qOs st_3TuKxmZ st_3Y6ESwY st_GnnuqFp st_1VMMH6S"})

    #scrolling until the time of the dive is more than 1 hour
    while len(divtime[(len(divtime)-1)].get_text()) <= 3:
        driver.execute_script('window.scrollBy(0, 30000)')
        element = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'st_3SL2gug'), ""))
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        mentions = soup.findAll(True, {"class": ["st_3SL2gug"]})
        divtime = soup.findAll(True, {"class":"st_28bQfzV st_1E79qOs st_3TuKxmZ st_3Y6ESwY st_GnnuqFp st_1VMMH6S"})
    count = 0
    #counting the number of mentions in the last hour
    for x in range (len(divtime)-1):
        if len(divtime[x].get_text()) <= 3:
            count = count + 1

    #-----------this is where sentiment AI work is going to have to go
    neutralCount = 0
    positiveCount = 0
    negativeCount = 0
    sid = SentimentIntensityAnalyzer()
    for x in range(count):
        ss = sid.polarity_scores(mentions[x].get_text())
        if ss["compound"] == 0.0:
            neutralCount += 1
        elif ss["compound"] > 0.0:
            positiveCount += 1
        else:
            negativeCount += 1


    #------------ END OF scrape, OUTPUT begins here, subject to change

    #symbol string from url
    symString = url[30:]
    ScrapedData = {}
    ScrapedData['mentions'] = count
    ScrapedData['time'] = timeStart
    ScrapedData["source"] = "stocktwits"
    ScrapedData["positive"] = positiveCount
    ScrapedData["negative"] = negativeCount
    ScrapedData["neutral"] = neutralCount


    with open(fn, "r") as file1:
        data = json.load(file1)

    for i in data:
        if i["_name"] == symString:
            i["_mentions"]["day"]["scrapes"].append(ScrapedData)
            i["_mentions"]["day"]["total"] += count
    
    with open(fn, "w") as file1:
        json.dump(data, file1)


driver.quit()
