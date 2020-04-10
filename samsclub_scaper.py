#the file for scraping sams club websites
#website link for TP: https://www.samsclub.com/s/toilet%20paper

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.samsclub.com/s/toilet%20paper/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

#array to hold all the prices
prices = []

for divss in soup.find_all('div', {'class': 'sc-channel-price'}):
     spans = divss.find('span', {'class': 'visuallyhidden'})
     prices.append(spans.text)
print(prices)