import uuid
import time
import datetime
import os
import os.path
from lxml import etree
import requests
import csv
import sys
import hashlib
import time
import urllib2
import json
from array import array

m = hashlib.md5()
m.update("clorox0305")

storeFeed = 'storeList.csv'

filename = 'Kingsford_static_Feed.csv'

def SetFromFeed(filename_open):
    temp = []

    with open(filename_open, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row)

    return temp

print "http://service.weatheralpha.com:9898/clorox/" + m.hexdigest() + "/zip/10003"

storeList = SetFromFeed(storeFeed)
feedList = []
feedList.append(storeList[0])

with open(filename, 'wb') as csvfile:
    writer = csv.writer(csvfile)

for i in range(0, len(storeList)):
    url = urllib2.urlopen("http://service.weatheralpha.com:9898/clorox/" + m.hexdigest() + "/zip/" + storeList[i][4])
    content = url.read()
    data=json.loads(content)

    if (data['result']['day_1_warm_high'] == 1 or data['result']['day_2_warm_high'] == 1 or data['result']['day_3_warm_high'] == 1 or data['result']['day_4_warm_high'] == 1):

        feedList.append(storeList[i])

        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(feedList[-1])