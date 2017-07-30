# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

"""
 The next couple lines will create the actual application instance and
 initialize it with the config from the same file in flaskr.py:
"""
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


"""
Lastly, you will add a method that allows for easy connections to the
specified database. This can be used to open a connection on request and
also from the interactive Python shell or a script. This will come in
handy later. You can create a simple database connection through SQLite
and then tell it to use the sqlite3.Row object to represent rows. This
allows the rows to be treated as if they were dictionaries instead of tuples.
"""

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
