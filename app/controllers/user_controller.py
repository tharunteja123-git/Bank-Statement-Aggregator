from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.

    This endpoint allows users to register a new account by providing the necessary information in the request body.

    Parameters:
        data (dict): A dictionary containing the user registration data.

    Returns:
        A JSON response with a success message if the user is registered successfully, or an error message if an exception occurs.

    Raises:
        Exception: If an error occurs during the registration process.

    Example Usage:
        POST /register
        {
            "username": "john_doe",
            "password": "password123",
            "email": "john.doe@example.com"
        }
    """
    data = request.get_json()
    try:
        UserService.register(data)
        return jsonify({'message': 'User registered successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = UserService.login(data)
        return jsonify(user), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500