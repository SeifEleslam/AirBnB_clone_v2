#!/usr/bin/python3
"""0 FLask Web APP"""
from flask import Flask
app = Flask(__name__)


@app.route("/airbnb-onepage")
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000', True)
