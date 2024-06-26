#!/usr/bin/python3
"""7 FLask Web APP"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_storage(exception):
    """Close the database connection."""
    storage.close()


@app.route("/cities_by_states")
def list_cities_by_states():
    """List all states in the database."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000')
