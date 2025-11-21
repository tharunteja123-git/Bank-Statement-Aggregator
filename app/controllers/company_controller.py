from flask import Blueprint, request, jsonify
from app.services.company_service import CompanyService

company_bp = Blueprint('company_bp', __name__)


@company_bp.route('/companies', methods=['POST'])
def add_company():
    """
    Add a new company.

    This endpoint allows the user to add a new company to the system.

    Parameters:
        data (dict): A dictionary containing the company data.

    Returns:
        A JSON response with a success message if the company is added successfully, or an error message if an exception occurs.

    Raises:
        Exception: If an error occurs while adding the company.

    Example Usage:
        POST /companies
        {
            "name": "ABC Company",
            "address": "123 Main St",
            "city": "New York",
            "country": "USA"
        }
    """
    data = request.get_json()
    try:
        CompanyService.add_company(data)
        return jsonify({'message': 'Company added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@company_bp.route('/companies', methods=['GET'])
def get_companies():
    try:
        companies = CompanyService.get_companies()
        return jsonify(companies), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
