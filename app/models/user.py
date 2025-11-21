from app.utils.db import db


class User(db.Model):
    """
    Represents a user in the system.

    Attributes:
        user_id (int): The unique identifier of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        company_id (int): The ID of the company the user belongs to.

    """

    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company.company_id'), nullable=False)
