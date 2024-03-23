#!/usr/bin/python3
"""7 FLask Web APP"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list", strict_slashes=False)
def hello_hbnb():
    states = map(lambda itm: itm[1], storage.all(State).items())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000', True)
