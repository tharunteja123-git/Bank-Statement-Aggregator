from flask import Blueprint, request, jsonify
from app.services.branch_service import BranchService

branch_bp = Blueprint('branch_bp', __name__)


@branch_bp.route('/branches', methods=['POST'])
def add_branch():
    """
    Add a new branch.

    This endpoint allows the user to add a new branch to the system.

    Parameters:
        data (dict): A dictionary containing the branch data.

    Returns:
        A JSON response with a success message if the branch is added successfully,
        or an error message if an exception occurs.

    Raises:
        Exception: If an error occurs while adding the branch.

    Example Usage:
        POST /branches
        {
            "name": "New Branch",
            "location": "City",
            "manager": "John Doe"
        }
    """
    data = request.get_json()
    try:
        BranchService.add_branch(data)
        return jsonify({'message': 'Branch added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@branch_bp.route('/branches', methods=['GET'])
def get_branches():
    try:
        branches = BranchService.get_branches()
        return jsonify(branches), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
