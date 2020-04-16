# Scraping for Kroger supermarket/retail store!
# Nadya Postolaki

import requests
from bs4 import BeautifulSoup



#Toilet Paper



print('Toilet Paper:')

result = requests.get("https://www.heb.com/search/?q=toilet+paper")
src = result.content
soup = BeautifulSoup(src, 'lxml')

print(soup.title) #this is the title thing I was talking about, it prints other sites' titles, but not kroger for some reason

prices = []

#for divss in soup.find_all('div', {'class': 'ProductCard'}):
#	spans = divvs.find('span', {'class': 'kds-Price-singular'})
#	prices.append(spans.text)

#print(prices)

print('This will appear after prices have been printed')

