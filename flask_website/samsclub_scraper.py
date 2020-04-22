import requests
from bs4 import BeautifulSoup

def getProducts(url):
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    baseURL = 'http://www.samsclub.com'

    # Open a file for data output
    file = open("output.csv","w")

    # Write the table headers
    file.write("Product;Price;Image\n")

    # Get all of the product cards from the search results page
    productCards = soup.find_all('div', {'class' :  lambda x: x and
        x.startswith('sc-product-card sc-product-card-grid')})

    # Extract data from each of the product cards
    for productCard in productCards:

        # Get the name of this product
        productName = productCard.find('div', {'class' : 'sc-product-card-title'}).find('span').text

        # Get the link to this product
        productLink = baseURL + productCard.find('a', {'class' : 'sc-product-card-pdp-link'})['href']

        # Get the price of this product
        # If a price can't be found, it will be "Unavailable"
        productPrice = 'Unavailable'
        for divs in productCard.find_all('div', {'class': 'sc-channel-price'}):
            spans = divs.find('span', {'class': 'visuallyhidden'})
            if spans is not None:
                productPrice = spans.text.replace('current price: ', '')

        # Get the image of this product
        imageWrapper = productCard.find('img', {'class': 'sc-product-card-image'})
        productImage = imageWrapper["src"].split("src=")[-1]
        if productImage == '':
            productImage = imageWrapper["data-src"].split("data-src=")[-1]

<<<<<<< HEAD:flask_website/samsclub_scraper.py
        # Append this products
        # Commas need to be removed so there aren't
        #   extra columns created in the .csv file
        nameLine += removeCommas(productName) + ","
        linkLine += removeCommas(productLink) + ","
        priceLine += removeCommas(productPrice) + ","
        imageLine += "<img src=\"" + productImage + "\">" + ","

    # Write the products' data to output.csv
    file.write(nameLine + "\n" +
                linkLine + "\n" +
                priceLine + "\n" +
                imageLine + "\n")
=======
        # Write this product's data to output.csv
        file.write("<a href=\"" + productLink + "\">" + productName.replace(";","") + "</a>;"
                    + productPrice + ";<img src=\"" + productImage + "\">\n")
>>>>>>> a73acd4f1d16d218b948f44a41c1fc45b00a03d3:flask_website/samsclub_scraper.py

    # Close the output file
    file.close()

def searchForProducts(query):
<<<<<<< HEAD:flask_website/samsclub_scraper.py
    getProducts('http://www.samsclub.com/s/' + query.replace(' ', '%20'))

def removeCommas(str):
    return str.replace(',', ' ')
=======
    getProducts('http://www.samsclub.com/s/' + query.replace(' ', '%20'))
>>>>>>> a73acd4f1d16d218b948f44a41c1fc45b00a03d3:flask_website/samsclub_scraper.py
