from lxml import html
import requests
import csv
import time
from datetime import datetime
import os
import json

url = ''
lowes = []
city = []
state = []
weather = []
historyweather = []
precipitation = []

filename = 'lowes_weather_feed.csv'

def setStores():
    with open('lowes_3.09.15_input.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            city.append(row[2])
            state.append(row[3])
            lowes.append(row)

    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)

def writeData(x=0):
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(lowes[x])


setStores()

for i in range(0, len(lowes)):
    #set url
    url = 'http://api.wunderground.com/api/28402eac81f4c2ed/almanac/q/' + state[i] + '/' + city[i] + '.json'

    #print url
    api = requests.get(url)
    apitext = api.text
    weatherapi = json.loads(apitext)

    #print weatherapi['almanac']['temp_high']['normal']['F']
    try:
        lowes[i].append(weatherapi['almanac']['temp_high']['normal']['F'])
    except:
        lowes[i].append('')

    url = 'http://api.wunderground.com/api/28402eac81f4c2ed/forecast/q/' + state[i] + '/' + city[i] + '.json'
    api = requests.get(url)
    apitext = api.text
    weatherapi = json.loads(apitext)

    #print weatherapi['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit']
    try:
        lowes[i].append(weatherapi['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit'])
    except:
        lowes[i].append('')

    #print weatherapi['forecast']['simpleforecast']['forecastday'][1]['pop']
    try:
        lowes[i].append(weatherapi['forecast']['simpleforecast']['forecastday'][1]['pop'])
    except:
        lowes[i].append('')

    writeData(i)

print 'File Completed'


#go through each store
#set url based on state and city
#grab weather and historical weather
#append weather to each row
#write current row