#the file for scraping sams club websites
#website link for TP: https://www.samsclub.com/s/toilet%20paper

import requests
from bs4 import BeautifulSoup

##########---Toilet Paper---#############
print('----------------TP-------------------')

result = requests.get("https://www.samsclub.com/s/toilet%20paper/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

####get prices
#array to hold all the prices
prices = []

for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
     spans = divss.find('span', {'class': 'visuallyhidden'})
     if spans is not None:
          prices.append(spans.text)
print(prices)


#####parce prices


#####get images
images = []
for divys in soup.find_all('div', {'class': 'sc-image-wrapper'}):
     imgs = divys.find('img', {'class': 'sc-product-card-image'})
     #finds the image source only if there is something there
     if imgs is not None:

          link = imgs["data-src"].split("data-src=")[-1]
          if link is '':
               link = imgs["src"].split("src=")[-1]

          images.append(link)
print(images)

####get names
#array to hold all the prices
names = []

for dives in soup.find_all('div', {'class': 'sc-product-card-title'}):
     spanss = dives.find('span')
     names.append(spanss.text)
print(names)



##########---Hand Sanitizer---#############
print('----------------Hand Sanitizer-------------------')

result = requests.get("https://www.samsclub.com/s/hand%20sanitizer")
src = result.content
soup = BeautifulSoup(src, 'lxml')


#####get images
images = []
for divys in soup.find_all('div', {'class': 'sc-image-wrapper'}):
     imgs = divys.find('img', {'class': 'sc-product-card-image'})
     #finds the image source only if there is something there
     if imgs is not None:

          link = imgs["data-src"].split("data-src=")[-1]
          if link is '':
               link = imgs["src"].split("src=")[-1]

          images.append(link)
print(images)

####get names
#array to hold all the prices
names = []

for dives in soup.find_all('div', {'class': 'sc-product-card-title'}):
     spanss = dives.find('span')
     names.append(spanss.text)
print(names)

####get prices
#array to hold all the prices
prices = []

for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
     spans = divss.find('span', {'class': 'visuallyhidden'})
     if spans is not None:
          prices.append(spans.text)
print(prices)


#####parce prices


##########---Soap---#############
print('----------------Soap-------------------')

result = requests.get("https://www.samsclub.com/s/soap")
src = result.content
soup = BeautifulSoup(src, 'lxml')


#####get images
images = []
for divys in soup.find_all('div', {'class': 'sc-image-wrapper'}):
     imgs = divys.find('img', {'class': 'sc-product-card-image'})
     #finds the image source only if there is something there
     if imgs is not None:

          link = imgs["data-src"].split("data-src=")[-1]
          if link is '':
               link = imgs["src"].split("src=")[-1]

          images.append(link)
print(images)

####get names
names = []

for dives in soup.find_all('div', {'class': 'sc-product-card-title'}):
     spanss = dives.find('span')
     names.append(spanss.text)
print(names)

####get prices
#array to hold all the prices
prices = []

for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
     spans = divss.find('span', {'class': 'visuallyhidden'})
     if spans is not None:
          prices.append(spans.text)
print(prices)


#####parce prices