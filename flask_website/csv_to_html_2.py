# Converting our output.csv to html
# April 21st, 2020

import sys
import csv
#import samsclub_scraper.py -- will need to uncomment this one and replace the above once we change the name.
import pandas as pd
sys.path.insert(1, 'C:/Users/wongp/Documents/Github/python_webscrapping/samsclub_scaper.py') # import samsclub_scaper.py

# grab output.csv
#csv_file = open('C:/Users/wongp/Documents/Github/python_webscrapping/flask_website/output.csv', 'r') # this file path will change depending on their own PC path(s)
a = pd.read_csv('C:/Users/wongp/Documents/Github/python_webscrapping/flask_website/output.csv', 'r')
a.to_html("Table.htm")
html_file = a.to_html()
