# Front-end for hackathon
# flask python

from flask import Flask, render_template, redirect, url_for
import sys
import samsclub_scraper
app = Flask(__name__) # app is an instance of the flask class.

# *** Start: Sam's Club Routing *** #
@app.route('/') # route decorator tells flask which URL to go through.
def home():
    return render_template('sc_home.html')

@app.route('/sc_tp')
def sc_tp():
    return render_template('sc_tp.html')

@app.route('/sc_soap')
def sc_soap():
    return render_template('sc_soap.html')

@app.route('/sc_handsanitizer')
def sc_handsanitizer():
    return render_template('sc_handsanitizer.html')
# *** End: Sam's Club Routing *** #

# *** Start: Walmart Routing *** #
@app.route('/walmart')
def wal_home():
    return render_template('wal_home.html')

@app.route('/wal_tp')
def wal_tp():
    return render_template('wal_tp.html')

@app.route('/wal_soap')
def wal_soap():
    return render_template('wal_soap.html')

@app.route('/wal_handsanitizer')
def wal_handsanitizer():
    return render_template('wal_handsanitizer.html')
# *** End: Walmart Routing *** #

@app.route('/about')
def sc_about():
    return render_template('about.html')

if __name__ == "__main__":
    #app.run()
    app.run(debug=True) # uncomment for debugging
