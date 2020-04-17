#the file for scraping sams club websites

#dependencies used to scrape websites
import requests
from bs4 import BeautifulSoup

#function to get price of item
def getPrices():
    prices = []
    for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
        spans = divss.find('span', {'class': 'visuallyhidden'})
        #finds the price if something is there
        if spans is not None:
            prices.append(spans.text)
    print(prices)
    return prices

#function to get image of item
def getImgs():
    images = []
    #checking for image of all the items
    for divys in soup.find_all('div', {'class': 'sc-image-wrapper'}):
        imgs = divys.find('img', {'class': 'sc-product-card-image'})
        #finds the image source only if there is something there
        if imgs is not None:
            link = imgs["data-src"].split("data-src=")[-1]
            link2 = imgs["src"].split("src=")[-1]
            if link is '':
                images.append(link2)
            if link2 is '':
                images.append(link)
    print(images)

#function to get name of item
def getNames():
    names = []
    #checking for the name of all the items
    for dives in soup.find_all('div', {'class': 'sc-product-card-title'}):
        spanss = dives.find('span')
        names.append(spanss.text)
    print(names)


####using the functions
print('----------------TP-------------------')
result = requests.get("https://www.samsclub.com/s/toilet%20paper/")
src = result.content
soup = BeautifulSoup(src, 'lxml')
getPrices()
getImgs()
getNames()


print('----------------Hand Sanitizer-------------------')
result = requests.get("https://www.samsclub.com/s/hand%20sanitizer")
src = result.content
soup = BeautifulSoup(src, 'lxml')
getPrices()
getImgs()
getNames()


print('----------------Soap-------------------')
result = requests.get("https://www.samsclub.com/s/soap")
src = result.content
soup = BeautifulSoup(src, 'lxml')
getPrices()
getImgs()
getNames()
