from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uuid
import time
import datetime
import os
import os.path
from lxml import etree
import requests
import csv
import sys
from selenium.webdriver.common.by import By

zipFeed = 'houstonZips.csv'
filename = 'dollarGeneral_Feed.csv'

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

feedList = []

driver = webdriver.Firefox()
driver.get("http://www.dollargeneral.com/storeLocator/")
for i in range(0, len(zipList)):	
	elem = driver.find_element_by_id("store-search-zip")
	elem.clear()
	elem.send_keys(zipList[i][0])
	elem.send_keys(Keys.RETURN)

	time.sleep(15)
	try:
		address = driver.find_element(By.XPATH, '//*[@id="store-list-0"]/div[2]/p[1]/span[1]').text
	
		try:
			city = driver.find_element(By.XPATH, '//*[@id="store-list-0"]/div[2]/p[1]/span[3]').text
		except Exception, e:
			city = driver.find_element(By.XPATH, '//*[@id="store-list-0"]/div[2]/p[1]/span[2]').text

		print zipList[i][0]
		print address
		print city

		feedList.append(zipList[i])
		feedList[-1].append(address)
		feedList[-1].append(city)

		with open(filename, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(feedList[-1])
	except Exception, e:
		pass

print("Done")