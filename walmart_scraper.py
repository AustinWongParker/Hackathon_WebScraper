# Web Scraping for Walmart
# Author: Austin Wong-Parker
# Date: 4 - 8 - 2020

# lxml is our parser.

import bs4
import requests
from bs4 import BeautifulSoup

'''
** From bs4 docs:
The BeautifulSoup object represents the parsed document as a whole.
For most purposes, you can treat it as a Tag object.
This means it supports most of the methods described in Navigating the tree and Searching the tree.
'''

def priceWithFulfillment(): # Parses prices for class=product-price-with-fulfillment
    prices = []
    for divss in soup.find_all('span', {'class': 'price display-inline-block arrange-fit price price-main'}):
         spans = divss.find('span', {'class': 'price-group'})
         if spans is not None:
             prices.append(spans.text)
    print(prices)
    return prices



def grab_image():
    images = []
    for divys in soup.find_all('div', {'class': 'page-wrapper'}):
        imgs = divys.find('img', {'data-pnodetype': 'item-pimg'})
        #finds the image source only if there is something there
        if imgs is not None:
            link = imgs["data-image-src"].split("data-image-src=")[-1]
            link2 = imgs["srcset"].split("srcset=")[-1]
            if link is '':
                images.append(link2)
            if link2 is '':
                images.append(link)

    print(images)

def grab_name():
    names = []

####using the functions
print('----------------TP-------------------')
result = requests.get("https://www.walmart.com/search/?query=toilet%20paper")
src = result.content
soup = BeautifulSoup(src, 'lxml')
priceWithFulfillment()
print('\n')
grab_image()
#grab_name()


print('----------------Hand Sanitizer-------------------')
result = requests.get("https://www.walmart.com/search/?query=hand%20sanitizer&typeahead=hand%20s")
src = result.content
soup = BeautifulSoup(src, 'lxml')
priceWithFulfillment()
print('\n')
#grab_image()
#grab_name()


print('----------------Soap-------------------')
result = requests.get("https://www.walmart.com/search/?query=soap")
src = result.content
soup = BeautifulSoup(src, 'lxml')
priceWithFulfillment()
print('\n')
#grab_image()
#grab_name()
#grab_image()




    #for
    #price = soup.find_all('div', {'class': 'product-price-with-fulfillment'})#[0].find('span').text
    #price = soup.find_all('div', {'class': 'price-group'})
    #print(price) # Just to see it on the screen / cmd for testing purposes
    #return price



'''

#the file for scraping sams club websites
#website link for TP: https://www.samsclub.com/s/toilet%20paper

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.samsclub.com/s/toilet%20paper/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

# urls = []
# for h2_tag in soup.find_all('h2'):
#     a_tag = h2_tag.find('a')
#     urls.append(a_tag.attrs['href'])

# price = soup.find_all('div', {'class': 'sc-channel-price'})[0].find_all('span', {'class': 'Price-group'}).title
price = soup.find_all('span', {'class': 'Price-group'})[0].title
print(price)
    # print(price) # Just to see it on the screen / cmd for testing purposes
    # return price

costs = []
# for spans in soup.find_all('span', {'class': 'Price-group'}):
#     costs.append(spans.title)

for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
     spans = divss.find('span', {'class': 'visuallyhidden'})
     costs.append(spans.text)
print(costs)

'''




''' # If we want a continous stream of data, a while loop will prob be our best bet.
while True:
    print('Current price: ' + str(parsePrice()))
'''



'''
Misc Code:

price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
return price

'''
