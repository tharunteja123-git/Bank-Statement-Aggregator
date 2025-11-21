from flask import Blueprint, request, jsonify
from app.services.bank_statement_service import BankStatementService

statement_bp = Blueprint('statement_bp', __name__)


@statement_bp.route('/generate_statement', methods=['POST'])
def generate_statement():
    """
    Generate a bank statement.

    This function is responsible for generating a bank statement based on the provided data.

    Parameters:
    - data (dict): A dictionary containing the necessary data for generating the statement.

    Returns:
    - response (json): A JSON response containing the result of the statement generation process.

    Raises:
    - Exception: If an error occurs during the statement generation process.

    Example Usage:
        data = {
            'account_number': '1234567890',
            'start_date': '2022-01-01',
            'end_date': '2022-01-31'
        }
        generate_statement(data)
    """
    data = request.get_json()
    try:
        BankStatementService.generate_statement(data)
        return jsonify({'message': 'Statement generated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@statement_bp.route('/upload_statement', methods=['POST'])
def upload_statement():
    data = request.get_json()
    try:
        BankStatementService.upload_statement(data)
        return jsonify({'message': 'Statement uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
