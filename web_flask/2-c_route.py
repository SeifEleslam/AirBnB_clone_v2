#!/usr/bin/python3
"""2 FLask Web APP"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is_(text: str):
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000', True)
