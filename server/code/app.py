#!/usr/bin/env python3

from flask import Flask

"""
Server to show the data of this experiment
"""


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"