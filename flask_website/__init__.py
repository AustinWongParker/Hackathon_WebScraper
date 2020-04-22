# Backend for hackathon - routing via Flask Python

import sys
from flask import Flask, render_template, redirect, url_for
from samsclub_scraper import *
from csv_to_html import *
app = Flask(__name__) # app is an instance of the flask class.

# *** Start: Sam's Club Routing *** #
@app.route('/') # route decorator tells flask which URL to go through.
def home():
    return render_template('sc_home.html')

@app.route('/sc_tp')
def sc_tp():
    sc_searchForProducts("Toilet Paper")
    convertFile("output.csv", "templates/table.html")
    return render_template('sc_tp.html')

@app.route('/sc_soap')
def sc_soap():
    sc_searchForProducts("Soap")
    convertFile("output.csv", "templates/table.html")
    return render_template('sc_soap.html')

@app.route('/sc_handsanitizer')
def sc_handsanitizer():
    sc_searchForProducts("Hand Sanitizer")
    convertFile("output.csv", "templates/table.html")
    return render_template('sc_handsanitizer.html')
# *** End: Sam's Club Routing *** #

# *** Start: Walmart Routing *** #
@app.route('/walmart')
def wal_home():
    return render_template('wal_home.html')

@app.route('/wal_tp')
def wal_tp():
    sc_searchForProducts("Toilet Paper") # Need to change to walmart. Will leave as SC for now
    convertFile("output.csv", "templates/table.html")
    return render_template('wal_tp.html')

@app.route('/wal_soap')
def wal_soap():
    sc_searchForProducts("Soap") # Need to change to walmart. Will leave as SC for now
    convertFile("output.csv", "templates/table.html")
    return render_template('wal_soap.html')

@app.route('/wal_handsanitizer')
def wal_handsanitizer():
    sc_searchForProducts("Hand Sanitizer") # Need to change to walmart. Will leave as SC for now
    convertFile("output.csv", "templates/table.html")
    return render_template('wal_handsanitizer.html')
# *** End: Walmart Routing *** #

# Search bar results #
@app.route('/?searched_result=') #+searched_string
def searched_result():
    return render_template('sc_searched_result.html')


# About page routing
@app.route('/about')
def sc_about():
    return render_template('about.html')

if __name__ == "__main__":
    #app.run()
    app.run(debug=True) # uncomment for debugging
