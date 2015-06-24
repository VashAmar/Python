#import boto
#from boto.s3.key import Key
import uuid
import time
import datetime
import os
import os.path
from lxml import etree
import requests
import csv
import sys

storeFeed = 'pandgZips.csv'

filename = 'pandg_Feed.csv'

def SetFromFeed(filename_open):
    temp = []

    with open(filename_open, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row)

    return temp

storeList = SetFromFeed(storeFeed)
feedList = []

with open(filename, 'wb') as csvfile:
    writer = csv.writer(csvfile)

for i in range(0, len(storeList)):

    url = 'http://api2.shoplocal.com/retail/64c64a1ed22cad25/2013.1/xml/RetailerTagListings?citystatezip='+storeList[i][4]+'&resultset=full&listingimagewidth=300&retailertagid=3476&sortby=6&pd=46BAB24B3A17EFABD7A68B3F4ACDEB34B2D5D393886015B49E685759418E61C45155806E9BF419E853D2FCD810781C'

    #storeElements[i].append(url)
    tree = etree.parse(url)

    #counts for sequence products
    price = tree.xpath('//Results[1]/Deal[1]/text()')
    #pricequalifier = tree.xpath('//collection[1]/data[1]/@pricequalifier')
    title = tree.xpath('//Results[1]/Title[1]/text()')
    image = tree.xpath('//Results[1]/ImageLocation[1]/text()')
    fineprint = tree.xpath('//Results[1]/FinePrint[1]/text()')
    price2 = tree.xpath('//Results[2]/Deal[1]/text()')
    #pricequalifier = tree.xpath('//collection[1]/data[1]/@pricequalifier')
    title2 = tree.xpath('//Results[2]/Title[1]/text()')
    image2 = tree.xpath('//Results[2]/ImageLocation[1]/text()')
    fineprint2 = tree.xpath('//Results[2]/FinePrint[1]/text()')

    if (len(price) > 0):
        feedList.append(storeList[i])
        feedList[-1].append(price[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        #feedList[-1].append(pricequalifier[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(title[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(image[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(fineprint[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(price2[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        #feedList[-1].append(pricequalifier[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(title2[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(image2[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
        feedList[-1].append(fineprint2[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))

        with open(filename, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(feedList[-1])

    #productline.append(fineprint[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))

'''
#login info for s3
AWS_ACCESS_KEY_ID = 'AKIAIDHB4LHE4VN52BSA'
AWS_SECRET_ACCESS_KEY = 'fDi6nTYM8Zt64NW76DF5j2KWkydP4qgd/N2U01xj'

#access s3
s3 = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

try:
    if (os.stat(filename) and '.csv' in filename):
        #set bucket/initial folder for s3
        bucket_name = "eyeview-prod-assets"
        bucket = s3.get_bucket(bucket_name)

        #set file to upload
        feedname = filename

        #set key to intial folder
        feedkey = Key(bucket)

        #set key -> filepath and file name to save as then upload feed to s3
        #feedkey.key = '17212/feed.csv'
        #feedkey.set_contents_from_filename(feedname)
    else:
        print "Wrong File Type"
except OSError:
    print "No File"
'''

print 'File Created'


#http://api.shoplocal.com/cvs/2012.2/xml/getretailertaglistings.aspx?campaignid=48c7d936d6e6611d%20&citystatezip=<PUT ZIP HERE>&resultset=full&listingimagewidth=300&retailertagid=2806&sortby=6&pd=46BBB2453F1DEDA3DCA4893D4ACDE154CABFA190956908C5E313284C4C8E60DB5250916F96FF06F551CCECB87D
