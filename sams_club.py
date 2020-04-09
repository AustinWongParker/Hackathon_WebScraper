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

urls = []
for spans in soup.find_all('span', {'class': 'Price-group'}).title:
    urls.append(spans)

print(urls)