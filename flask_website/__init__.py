# Front-end for hackathon
# flask python

from flask import Flask, render_template, redirect, url_for
import sys
import sams_funcs
app = Flask(__name__) # app is an instance of the flask class.

@app.route('/') # route decorator tells flask which URL to go through.
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tp')
def tp():
    return render_template('tp.html')

@app.route('/soap')
def soap():
    return render_template('soap.html')

@app.route('/handsanitizer')
def handsanitizer():
    return render_template('handsanitizer.html')


if __name__ == "__main__":
    #app.run()
    app.run(debug=True) # uncomment for debugging
