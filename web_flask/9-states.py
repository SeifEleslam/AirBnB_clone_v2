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


@app.route("/states/", defaults={'id': None})
@app.route("/states/<id>")
def list_cities_by_states(id):
    """List all states in the database."""
    state = None
    states = None
    if id:
        state = storage.all().get(f'State.{id}')
    else:
        states = storage.all(State).values()
    print(states)
    return render_template(
        '9-states.html',
        states=states, state=state, all=id is None)


if __name__ == '__main__':
    """Start running on http://localhost:5000/"""
    app.run('0.0.0.0', '5000')
