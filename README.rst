Movie Reviews
=============

A short description of the project.

This Project uses Sqlite3 as database.

Cloning the project
-------------------

Run below command to clone the project in your local::

    $ git clone https://github.com/sheeshmohsin/moviereviews


Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

You can now run the usual Django ``runserver`` command (replace ``yourapp`` with the name of the directory containing the Django project)::

    $ python yourapp/manage.py runserver

