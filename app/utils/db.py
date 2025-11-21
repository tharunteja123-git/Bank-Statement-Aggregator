from flask_sqlalchemy import SQLAlchemy

"""
This module provides a database utility for the bankStatementAggregator application.
The `db` object is an instance of the `SQLAlchemy` class from the `flask_sqlalchemy` package.
It is used to interact with the database and perform various database operations.
Usage:
	- Import the `db` object from this module.
	- Use the `db` object to define database models and perform database operations.
"""

db = SQLAlchemy()
