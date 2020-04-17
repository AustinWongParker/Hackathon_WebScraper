# OK SO APPARENTLY KROGER DOESN'T LIKE WEBSCRAPING
# Scraping for H-E-B bc Texas
# Nadya Postolaki

import requests
from bs4 import BeautifulSoup

print('Toilet Paper:')

result = requests.get("https://www.heb.com/search/?q=toilet+paper")
src = result.content
soup = BeautifulSoup(src, 'lxml')

prices = []

for divvs in soup.find_all('div', {'class': 'cat-price'}):
	spans = divvs.find('span', {'class': 'cat-price-number'})
	prices.append(spans.text)


#TO-DO: get rid of random characters in prices array.
for str in prices:
	newStr = str.replace('\n','').replace('each','').replace(' ','')
	print(newStr)




print(prices)
