# Flask Tutorial

The files inside of the static folder are available to users of the application via HTTP. This is the place where CSS and JavaScript files go. Inside the templates folder, Flask will look for Jinja2 templates.

***

### Database Schema

```sql
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
```

This schema consists of a single table called entries. Each row in this table has an id, a title, and a text. The id is an automatically incrementing integer and a primary key, the other two are strings that must not be null.

***

### Application Step Code

Now that the schema is in place, you can create the application module, flaskr.py. This file should be placed inside of the flaskr/flaskr folder. The first several lines of code in the application module are the needed import statements. After that there will be a few lines of configuration code. For small applications like flaskr, it is possible to drop the configuration directly into the module. However, a cleaner solution is to create a separate .ini or .py file, load that, and import the values from there.

Here are the import statements (in flaskr.py):

```
# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
```

The next couple lines will create the actual application instance and initialize it with the config from the same file in flaskr.py:

```python
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
```

The Config object works similarly to a dictionary, so it can be updated with new values.

```
** Database Path **

Operating systems know the concept of a current working directory for each process. Unfortunately, you cannot depend on this in web applications because you might have more than one application in the same process.

For this reason the app.root_path attribute can be used to get the path to the application. Together with the os.path module, files can then easily be found. In this example, we place the database right next to it.

For a real-world application, it’s recommended to use Instance Folders instead.
```

Usually, it is a good idea to load a separate, environment-specific configuration file. Flask allows you to import multiple configurations and it will use the setting defined in the last import. This enables robust configuration setups. from_envvar() can help achieve this.

```python
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
```

Simply define the environment variable FLASKR_SETTINGS that points to a config file to be loaded. The silent switch just tells Flask to not complain if no such environment key is set.

In addition to that, you can use the from_object() method on the config object and provide it with an import name of a module. Flask will then initialize the variable from that module. Note that in all cases, only variable names that are uppercase are considered.

The SECRET_KEY is needed to keep the client-side sessions secure. Choose that key wisely and as hard to guess and complex as possible.

Lastly, you will add a method that allows for easy connections to the specified database. This can be used to open a connection on request and also from the interactive Python shell or a script. This will come in handy later. You can create a simple database connection through SQLite and then tell it to use the sqlite3.Row object to represent rows. This allows the rows to be treated as if they were dictionaries instead of tuples.

```
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
```

***

### Installing flaskr as a package

Flask is now shipped with built-in support for Click. Click provides Flask with enhanced and extensible command line utilities. Later in this tutorial you will see exactly how to extend the flask command line interface (CLI).

A useful pattern to manage a Flask application is to install your app following the Python Packaging Guide. Presently this involves creating two new files; setup.py and MANIFEST.in in the projects root directory. You also need to add an __init__.py file to make the flaskr/flaskr directory a package. After these changes, your code structure should be:

```
/flaskr
    /flaskr
        __init__.py
        /static
        /templates
        flaskr.py
        schema.sql
    setup.py
    MANIFEST.in
```

The content of the setup.py file for flaskr is:

```python
from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
```

When using setuptools, it is also necessary to specify any special files that should be included in your package (in the MANIFEST.in). In this case, the static and templates directories need to be included, as well as the schema. Create the MANIFEST.in and add the following lines:

```
graft flaskr/templates
graft flaskr/static
include flaskr/schema.sql
```

To simplify locating the application, add the following import statement into this file, flaskr/__init__.py:

```
from .flaskr import app

```

This import statement brings the application instance into the top-level of the application package. When it is time to run the application, the Flask development server needs the location of the app instance. This import statement simplifies the location process. Without it the export statement a few steps below would need to be export FLASK_APP=flaskr.flaskr.

At this point you should be able to install the application. As usual, it is recommended to install your Flask application within a virtualenv. With that said, go ahead and install the application with:

```
pip install --editable .
```

The above installation command assumes that it is run within the projects root directory, flaskr/. The editable flag allows editing source code without having to reinstall the Flask app each time you make changes. The flaskr app is now installed in your virtualenv (see output of pip freeze).

With that out of the way, you should be able to start up the application. Do this with the following commands:

```
export FLASK_APP=flaskr
export FLASK_DEBUG=true
flask run
```

(In case you are on Windows you need to use set instead of export). The FLASK_DEBUG flag enables or disables the interactive debugger. Never leave debug mode activated in a production system, because it will allow users to execute code on the server!

You will see a message telling you that server has started along with the address at which you can access it.

When you head over to the server in your browser, you will get a 404 error because we don’t have any views yet. That will be addressed a little later, but first, you should get the database working.

**Externally Visible Server**

Want your server to be publicly available? Check out the [externally visible server section for more information](http://flask.pocoo.org/docs/0.12/quickstart/#public-server).
