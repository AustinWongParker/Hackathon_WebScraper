# Converting our output.csv to html
# April 21st, 2020

import sys
import csv
#import samsclub_scraper.py -- will need to uncomment this one and replace the above once we change the name.
from prettytable import PrettyTable # python module. need to download. pip install PrettyTable
sys.path.insert(1, 'C:/Users/wongp/Documents/Github/python_webscrapping/samsclub_scaper.py') # import samsclub_scaper.py

# grab output.csv
csv_file = open('C:/Users/wongp/Documents/Github/python_webscrapping/flask_website/output.csv', 'r') # this file path will change depending on their own PC path(s)
csv_file = csv_file.readlines() # creates an array of out the csv data
line_1 = csv_file[0] # first element is line 1
line_1 = line_1.split(',') # splits elements after each comma
line_2 = csv_file[1] # second element is line 2
line_1 = line_2.split(',') # splits elements after each comma

print(csv_file)

'''
line_3 = csv_file[2] # second element is line 3
line_4 = csv_file[3] # second element is line 4
'''
