#!/usr/bin/python3
"""7 FLask Web APP"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_storage(exception):
    """Close the database connection."""
    storage.close()


@app.route("/hbnb_filters")
def list_cities_by_states():
    """List all states in the database."""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html',
        states=states, amenities=amenities)


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000')
