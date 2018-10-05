[![Build Status](https://travis-ci.org/mariamiah/MyDiary-API-with-Database.svg?branch=develop)](https://travis-ci.org/mariamiah/MyDiary-API-with-Database)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8769914c94dcd4499614/test_coverage)](https://codeclimate.com/github/mariamiah/MyDiary-API-with-Database/test_coverage)
# MyDiary-API-With-Database
MyDiary is an online journal where users can pen down their thoughts and feelings.

## Features 
- Users can signup on the application
- Users can login into the application
- Users can view the contents of a diary entry
- Users can add a diary entry
- Users can modify a diary entry

## API Endpoints
| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| POST | /api/v1/signup | Registers a user |
| GET | api/v1/users | Fetches all users |
| POST | api/v1/diaries | Creates new diary |
| GET | api/v1/diaries | Fetches all diaries |
| GET | api/v1/diaries/&lt;diary_id&gt; | Fetches diary by id |
| DELETE | api/v1/diaries/&lt;diary_id&gt; | Deletes a diary |
| GET | api/v1/entries | Fetch all entries |
| POST | api/v1/entries | Create a diary entry |
| GET | api/v1/entries/&lt;entry_id&gt; | Fetch a specific entry  |
| PUT | api/v1/entries/&lt;entry_id&gt; | Update diary entry |

    
**Getting started with the app**

**Technologies used to build the application**

* [Python 3.6](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)


## Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone https://github.com/mariamiah/MyDiary-API-with-Database.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh
$ pip install -r requirements.txt
```

Start the application by running
```sh
$ python run.py
```

**Running tests**

* Install nosetests 
* navigate to project root
* Use `nosetests tests/` to run the tests
* To run tests with coverage, use `nosetests --with-coverage --cover-package=app && coverage report`


