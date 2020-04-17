#the file for scraping sams club websites
import requests
from bs4 import BeautifulSoup


def getPrices(soup):
    prices = []

    for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
        spans = divss.find('span', {'class': 'visuallyhidden'})
        if spans is not None:
            prices.append(spans.text)
    print(prices)
    return prices

def getImgs(soup):
    images = []
    for divys in soup.find_all('div', {'class': 'sc-image-wrapper'}):
        imgs = divys.find('img', {'class': 'sc-product-card-image'})
        #finds the image source only if there is something there
        if imgs is not None:
            link = imgs["data-src"].split("data-src=")[-1]
            link2 = imgs["src"].split("src=")[-1]
            if link == '':
                images.append(link2)
            if link2 == '':
                images.append(link)

    print(images)


def getNames(soup):
    names = []
    for dives in soup.find_all('div', {'class': 'sc-product-card-title'}):
        spanss = dives.find('span')
        names.append(spanss.text)
    print(names)

def getProducts(url):
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    getPrices(soup)
    getImgs(soup)
    getNames(soup)

def searchForProducts(query):
    getProducts('http://www.samsclub.com/s/' + query.replace(' ', '%20'))

# Testing
print('----------------TP-------------------')
searchForProducts('toilet paper')

print('----------------Hand Sanitizer-------------------')
searchForProducts('hand sanitizer')

print('----------------Soap-------------------')
searchForProducts('soap')