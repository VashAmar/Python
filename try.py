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


zipFeed = 'zipfeed.csv'
filename = 'edible_input.csv'

def SetFromFeed(filename_open):
    temp = []

    with open(filename_open, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row)
          
    return temp
    

feedlist = SetFromFeed(zipFeed)
finallist = []




driver = webdriver.Firefox()
driver.get("https://www.ediblearrangements.com/stores/StoreLocator.aspx?currloc=true")
txtbox = driver.find_element_by_id('txtSearchStore')
for i in range (0,len(feedlist)):

	txtbox.send_keys(feedlist[i])

	txtbox.send_keys(Keys.RETURN)
	time.sleep(1)	
	

	master = driver.find_element_by_id('ulStoresList')
	counter=0
	address = null
	city = null
	state = null
	zipcode = null
	phone = null
	temp = null
	data= []
	
	for store in master.find_elements_by_tag_name('li'):
		name = store.find_element_by_class_name('StoreListName').text
		fulladdress = store.find_element_by_class_name('StoreListAddress').text
		a,b,c=fulladdress.split('\n')
		address = a
		phone = c
		d,e = b.split(",")
		city = d
		f,g=e.split(" ")
		state= f
		zipcode = g
		counter = counter+1
		data.append(name)
		data.append(address)
		data.append(city)
		data.append(state)
		data.append(zipcode)
		if counter>=5:
			break
	finallist.append(data)
	with open(filename, 'a') as csvfile:
		
        writer = csv.writer(csvfile)
        writer.writerow(feedList[-1])
	