# TODOS_API

Todos_api is a Python Flask built REST API which enables one to create, read, update and delete their TODO tasks.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. A linux machine is assumed.

### Pre-requisites
* [Python](https://docs.python.org/3/) versions 2.7, 3.3 to 3.7
* [Git](https://git-scm.com/)
* [pip](https://pypi.python.org/pypi/pip)
* [PostgreSQL](https://www.postgresql.org/docs/current/static/tutorial.html)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

Ensure you have installed PostgreSQL in your computer and it's server is running locally on port 5432

### Installing

Clone the repo

```
$ git clone https://github.com/muhallan/todos_api.git
$ cd todos_api
```

Create the virtual environment

```
$ pip install virtualenv
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv todos
```

Create Postgres databases for use in testing and development

```
$ createdb test_todos_db
$ createdb todos
```

Create a file called `.env` in the root of the project paste in it the contents of `.env.sample`.
Modify the contents of `.env` especially the database uri to match the database path you've created.
Export the environment variables.

```
$ source .env
```
Install dependencies in the virtual environment

```
$ pip install -r requirements.txt
```

Set up the databases by running migrations
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
Run the API

```
$ python manage.py runserver
```

To access the API on the server, and interface with it, fire up Postman and run this url
http://localhost:5000/todos, select POST, and in the body, put parameters with keys *title* and *description*

### Running the tests

```
$ python manage.py test
```

## Author

**Muhwezi Allan**

