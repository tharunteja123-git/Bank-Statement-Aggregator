from app.repositories.user_repository import UserRepository


class UserService:
    """
    A service class for user-related operations.
    """

    @staticmethod
    def register(data):
        """
        Registers a user.

        Args:
            data (dict): A dictionary containing user data.

        Returns:
            None

        Raises:
            None
        """
        UserRepository.add_user(data)

    @staticmethod
    def login(data):
        """
        Logs in a user.

        Args:
            data (dict): A dictionary containing user login data.

        Returns:
            dict: A dictionary containing user data if login is successful.

        Raises:
            Exception: If login fails.
        """
        user = UserRepository.get_user_by_credentials(data)
        if not user:
            raise Exception("Invalid username or password")
        return user