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
