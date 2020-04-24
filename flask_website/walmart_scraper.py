import requests
from bs4 import BeautifulSoup

def getProducts(url):
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    baseURL = 'https://www.walmart.com/'

    # Open a file for data output
    file = open("output.csv","w")

    # Write the table headers
    file.write("Product;Price;Image\n")

    # Get all of the product cards from the search results page
    productCards = soup.find_all('div', {'class' :  'search-result-gridview-item-wrapper'})

    # Extract data from each of the product cards
    for productCard in productCards:
 
        productWrapper = soup.find('a', {'class' :  lambda x: x and
            x.startswith('product-title-link')})
        
        # Get the name of this product
        productName = productWrapper.find('span').text

        # Get the link to this product
        productLink = baseURL + productWrapper["href"]

        # Get the image of this product
        imageWrapper = productCard.find('div', {'class' : 'orientation-square'})
        productImage = imageWrapper.find('img')['data-image-src']

        # Get the price of this product
        # If a price can't be found, it will be "Unavailable"
        productPrice = 'Unavailable'
        priceWrapper = productCard.find('span', {'class' : 'price display-inline-block arrange-fit price price-main'})
        if priceWrapper != None:
            priceSpan = priceWrapper.find('span', {'class' : 'visuallyhidden'})
            if priceSpan != None:
                productPrice = priceSpan.text

        # Write this product's data to output.csv
        file.write("<a href=\"" + productLink + "\">" + productName.replace(";","") + "</a>;"
                    + productPrice + ";<img src=\"" + productImage + "\">\n")

    # Close the output file
    file.close()

def wal_searchForProducts(query):     
  getProducts('https://www.walmart.com/search/?query=' + query.replace(' ', '%20'))
