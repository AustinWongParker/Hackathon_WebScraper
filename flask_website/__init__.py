# Front-end for hackathon
# flask python

from flask import Flask, render_template, redirect, url_for
import sys
app = Flask(__name__) # app is an instance of the flask class.

@app.route('/') # route decorator tells flask which URL to go through.
def home():
    return render_template('layout.html')

if __name__ == "__main__":
    #app.run()
    app.run(debug=True) # uncomment for debugging
