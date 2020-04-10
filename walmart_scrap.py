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

result = requests.get("https://www.walmart.com/search/?query=toilet%20paper") # Need specific URL
src = result.content # This is the page content from the website.
soup = BeautifulSoup(src, 'lxml') # ** This is our soup object

def priceWithFulfillment(): # Parses prices for class=product-price-with-fulfillment
    #for
    #price = soup.find_all('div', {'class': 'product-price-with-fulfillment'})#[0].find('span').text
    price = soup.find_all('div', {'class': 'price-group'})
    print(price) # Just to see it on the screen / cmd for testing purposes
    return price

def grab_image():
    image = soup.find_all('div', {'class': 'orientation-square'})#[0].find('span').text
    print(image)
    return image





priceWithFulfillment()
#grab_image()





''' # If we want a continous stream of data, a while loop will prob be our best bet.
while True:
    print('Current price: ' + str(parsePrice()))
'''



'''
Misc Code:

price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
return price

'''
