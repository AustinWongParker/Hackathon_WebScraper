#the file for scraping sams club websites
import requests
from bs4 import BeautifulSoup


def getPrices():
    prices = []

    for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
        spans = divss.find('span', {'class': 'visuallyhidden'})
        if spans is not None:
            prices.append(spans.text)
    print(prices)
    return prices

def getImgs():
    images = []
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


def getNames():
    names = []
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
