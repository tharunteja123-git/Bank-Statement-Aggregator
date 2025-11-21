from app.models.user import User
from app.utils.db import db


class UserRepository:
    """
    This class represents a repository for managing user data.
    Methods:
        add_user(data): Adds a new user to the database.
        get_user_by_credentials(data): Retrieves a user from the database based on their credentials.
    """
    """
        Adds a new user to the database.
        Args:
            data (dict): A dictionary containing the user data.
        Returns:
            None
        """
    pass
    """
        Retrieves a user from the database based on their credentials.
        Args:
            data (dict): A dictionary containing the user credentials (email and password).
        Returns:
            User: The user object if found, None otherwise.
        """
    pass

    @staticmethod
    def add_user(data):
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get_user_by_credentials(data):
        user = User.query.filter_by(
            email=data['email'], password=data['password']).first()
        return user
