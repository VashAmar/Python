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

filename = 'cubcadet_Feed.csv'

address = []
zips = []

zipfile = 'allZips_cubcadet.csv'

def SetFromFeed(filename_open):
    temp = []

    with open(filename_open, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row)

    return temp

def CreateBlankFeed(filename_write):
    with open(filename_write, 'wb') as csvfile:
        writer = csv.writer(csvfile)

def WriteLineFeed(filename_write, curr_address):
    with open(filename_write, 'a') as csvfile:
        writer = csv.writer(csvfile)

        stateline = []
        stateline.append(curr_address)

        writer.writerow(stateline)

zips = SetFromFeed(zipfile)
CreateBlankFeed(filename)

feedList = []

driver = webdriver.Firefox()
driver.get("http://www.cubcadet.com/equipment/WhereToBuy?langId=-1&storeId=10051&catalogId=14101")
#assert "CubCadet" in driver.title

url = driver.current_url
print url

for z in zips:
	if str(int(z[0])) not in address:
		driver.get("http://www.cubcadet.com/equipment/WhereToBuy?catalogId=14101&storeId=10051&langId=-1&radius=5&zip=" + z[0])
		#time.sleep(0.1)
		#elem = driver.find_element_by_id("zip")
		#for i in range (0,5):
			#elem.send_keys(Keys.BACK_SPACE)
			#elem.send_keys(Keys.ARROW_LEFT)
			#elem.send_keys(Keys.DELETE)
		#elem.send_keys(z[0])
		#elem.send_keys(Keys.RETURN)
		#assert "No results found." not in driver.page_source

		#time.sleep(1)

		for i in range(0, 3):
			try:
				tempaddress = driver.find_element(By.XPATH, '//*[@id="' + str(i + 1) + '"]/div[1]').text
			except:
				break
			
			if tempaddress not in address:
				address.append(driver.find_element(By.XPATH, '//*[@id="' + str(i + 1) + '"]/div[1]').text)
				WriteLineFeed(filename, address[len(address) - 1])

#driver.save_screenshot('screenie.png')
driver.quit()

#print address[0]
#feedList[-1].append(addrees[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))
#feedList[-1].append(addrees[0].encode('utf-8').replace('\n', ' ').replace('\r', ''))

print("Done")