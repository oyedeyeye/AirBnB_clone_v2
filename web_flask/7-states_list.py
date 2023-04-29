#!/usr/bin/python3
"""script that starts a Flask web application:
application must be listening on 0.0.0.0, port 5000
use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
Routes:
/states_list: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: list of all State objects present in DBStorage sorted by name(A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B>
Import this 7-dump to have some data
You must use the option strict_slashes=False in your route definition
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """close the database connection"""
    storage.close()


@app.route('/states_list')
def states_list():
    """display a HTML page: (inside the tag BODY)
    H1: “States”
    UL: list of all State objects present in DBStorage sorted by name(A->Z)
    LI: description of one State: <state.id>: <B><state.name></B>"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
