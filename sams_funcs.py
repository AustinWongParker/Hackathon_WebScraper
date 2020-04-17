#the file for scraping sams club websites

#dependencies used to scrape websites
import requests
from bs4 import BeautifulSoup

#function to get price of item
def getPrices(soup):
    prices = []
    for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
        spans = divss.find('span', {'class': 'visuallyhidden'})
        #finds the price if something is there
        if spans is not None:
            prices.append(spans.text)
    print(prices)
    return prices

#function to get image of item
def getImgs(soup):
    images = []
    #checking for image of all the items
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

#function to get name of item
def getNames(soup):
    names = []
    #checking for the name of all the items
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