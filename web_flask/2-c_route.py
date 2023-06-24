#!/usr/bin/python3
"""third task"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display hello HBNB!"""
    return ("hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display hello HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display c and text"""
    return ("C %s" % (text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
