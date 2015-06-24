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
m.update("clorox0310")

storeFeed = 'storeList.csv'

filename = 'Kingsford_Feed.csv'

def SetFromFeed(filename_open):
    temp = []

    with open(filename_open, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row)

    return temp

storeList = SetFromFeed(storeFeed)
storeList1 = SetFromFeed(storeFeed)
storeList2 = SetFromFeed(storeFeed)
feedList = []
feedList.append(storeList[0])

print "http://service.weatheralpha.com:9898/clorox/" + m.hexdigest() + "/zip/10003"


with open(filename, 'wb') as csvfile:
    writer = csv.writer(csvfile)

for i in range(0, len(storeList)):
    url = urllib2.urlopen("http://service.weatheralpha.com:9898/clorox/" + m.hexdigest() + "/zip/" + storeList[i][4])
    content = url.read()
    data=json.loads(content)

    count = 0


    feedList.append(storeList[i])

    if (data['result']['day_2_warm_high'] == 1 and data['result']['48_rain_total'] == 0.00):
        Fridaytemp = data['result']['day_2_max']
        feedList[-1].append("Friday")
        feedList[-1].append(Fridaytemp)
        count+=1

        if(data['result']['day_2_cloud_cover']<30):
            feedList[-1].append("sunnyIcon")
        elif(data['result']['day_2_cloud_cover']<70):
            feedList[-1].append("pariallyCloudyIcon")
        elif(data['result']['day_2_cloud_cover']>70):
            feedList[-1].append("cloudyIcon")


    if (data['result']['day_3_warm_high'] == 1 and data['result']['day_3_cloud_cover'] < 50):
        Saturdaytemp = data['result']['day_3_max']
        feedList[-1].append("Saturday")
        feedList[-1].append(Saturdaytemp)
        count+=1

        if(data['result']['day_3_cloud_cover']<30):
            feedList[-1].append("sunnyIcon")
        elif(data['result']['day_3_cloud_cover']<50):
            feedList[-1].append("pariallyCloudyIcon")

    if (data['result']['day_4_warm_high'] == 1 and data['result']['day_4_cloud_cover'] < 50):
        Sundaytemp = data['result']['day_4_max']
        feedList[-1].append("Sunday")
        feedList[-1].append(Sundaytemp)
        count+=1

        if(data['result']['day_4_cloud_cover']<30):
            feedList[-1].append("sunnyIcon")
        elif(data['result']['day_4_cloud_cover']<50):
            feedList[-1].append("pariallyCloudyIcon")

    feedList[-1].append(count)
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(feedList[-1])

    feedList=[]
    feedList.append(storeList1[i])
    count = 0



    if (data['result']['day_3_warm_high'] == 1 and data['result']['day_3_cloud_cover'] < 50):
        Saturdaytemp = data['result']['day_3_max']
        feedList[-1].append("Saturday")
        feedList[-1].append(Saturdaytemp)
        count+=1

        if(data['result']['day_3_cloud_cover']<30):
            feedList[-1].append("sunnyIcon")
        elif(data['result']['day_3_cloud_cover']<50):
            feedList[-1].append("pariallyCloudyIcon")

    if (data['result']['day_4_warm_high'] == 1 and data['result']['day_4_cloud_cover'] < 50):
        Sundaytemp = data['result']['day_4_max']
        feedList[-1].append("Sunday")
        feedList[-1].append(Sundaytemp)
        count+=1

        if(data['result']['day_4_cloud_cover']<30):
            feedList[-1].append("sunnyIcon")
        elif(data['result']['day_4_cloud_cover']<50):
            feedList[-1].append("pariallyCloudyIcon")

    feedList[-1].append(count)

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(feedList[-1])

    feedList=[]
    feedList.append(storeList2[i])
    count = 0


    if (data['result']['day_4_warm_high'] == 1 and data['result']['day_4_cloud_cover'] < 50):
        Sundaytemp = data['result']['day_4_max']
        feedList[-1].append("Sunday")
        feedList[-1].append(Sundaytemp)
        count+=1

        if(data['result']['day_4_cloud_cover']<30):
            feedList[-1].append("sunnyIcon")
        elif(data['result']['day_4_cloud_cover']<50):
            feedList[-1].append("pariallyCloudyIcon")

    feedList[-1].append(count)

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(feedList[-1])

print "Done"