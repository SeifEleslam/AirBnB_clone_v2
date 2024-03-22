#!/usr/bin/python3
"""6 FLask Web APP"""
from flask import Flask, render_template
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


@app.route("/python/", defaults={'text': 'is cool'})
@app.route('/python/<text>')
def py_is_(text: str):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>')
def int_only(n: int):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def int_only_template(n: int):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def int_even_or_odd_template(n: int):
    return render_template(
        '6-number_odd_or_even.html',
        n=n, des='even'if n % 2 == 0 else 'odd')


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000', True)
