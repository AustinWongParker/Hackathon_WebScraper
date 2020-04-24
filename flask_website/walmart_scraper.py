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
    # for divss in soup.find_all('span', {'class': 'price display-inline-block arrange-fit price price-main'}):
    #      spans = divss.find('span', {'class': 'price-group'})
    for divvs in soup.find_all('div', {'class': 'product-price-with-fulfillment'}):
        if divvs is not None:
            divss = divvs.find('span', {'class': 'price display-inline-block arrange-fit price price-main'})
            if divss is not None:
                spans = divss.find('span', {'class': 'visuallyhidden'})
                if spans is not None:
                    prices.append(spans.text)
                else:
                    prices.append('');
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
    for grids in soup.find_all('div', {'class': 'search-result-gridview-item-wrapper'}):
        # dives = grids.find('a', {'class': 'product-title-link line-clamp line-clamp-2'})
        dives = grids.find('div', {'class': 'search-result-product-title gridview'})
        ives = dives.find('a', {'class': 'product-title-link line-clamp line-clamp-2 truncate-title'})
        if ives is not None:
            spanss = ives.find('span')
            names.append(spanss.text)
        else:
            names.append(' ');
    print(names)

####using the functions
print('----------------TP-------------------')
result = requests.get("https://www.walmart.com/search/?query=toilet%20paper")
src = result.content
soup = BeautifulSoup(src, 'lxml')
priceWithFulfillment()
print('\n')
grab_image()
grab_name()


print('----------------Hand Sanitizer-------------------')
result = requests.get("https://www.walmart.com/search/?query=hand%20sanitizer&typeahead=hand%20s")
src = result.content
soup = BeautifulSoup(src, 'lxml')
priceWithFulfillment()
print('\n')
#grab_image()
grab_name()


print('----------------Soap-------------------')
result = requests.get("https://www.walmart.com/search/?query=soap")
src = result.content
soup = BeautifulSoup(src, 'lxml')
priceWithFulfillment()
print('\n')
#grab_image()
grab_name()
# grab_image()