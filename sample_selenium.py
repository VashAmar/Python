from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uuid
import time
import datetime
import os
import os.path
from lxml import etree
#import requests
import csv
import sys
from selenium.webdriver.common.by import By

zipFeed = 'zips.csv'
filename = 'costco_Feed.csv'

def SetFromFeed(filename_open):
    temp = []

    with open(filename_open, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row)

    return temp

zipList = SetFromFeed(zipFeed)
feedList = []

with open(filename, 'wb') as csvfile:
    writer = csv.writer(csvfile)

driver = webdriver.Firefox()
driver.get("http://m.costco.com/WarehouseLocatorView?storeId=10301&catalogId=10003&langId=-1")

for i in range(0, len(zipList)):

	assert "Costco" in driver.title
	elem = driver.find_element_by_id("txtLocation")
	elem.clear()
	elem.send_keys(zipList[i][0])
	elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source

	url = driver.current_url
	print url

	time.sleep(1)

	address = driver.find_element(By.XPATH, '//*[@id="warehouseDetails"]/tr[1]/td[2]/span/span/div[1]').text
	city = driver.find_element(By.XPATH, '//*[@id="warehouseDetails"]/tr[1]/td[2]/span/span/div[2]').text

	print address
	print city

	feedList.append(zipList[i])
	feedList[-1].append(address)
	feedList[-1].append(city)

	with open(filename, 'a') as csvfile:
	    writer = csv.writer(csvfile)
	    writer.writerow(feedList[-1])

print("Done")