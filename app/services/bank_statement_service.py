from datetime import datetime
import os
from app.repositories.branch_repository import BranchRepository
from app.utils.s3 import S3Client
from app.repositories.bank_statement_repository import BankStatementRepository
from app.repositories.transaction_repository import TransactionRepository
from app.utils.parser import Parser
from scripts.generate_transactions import generate_random_transactions


class BankStatementService:
    """
    A class that provides methods for generating and uploading bank statements.
    Methods:
    - generate_statement(data): Generates a bank statement in CSV format based on the provided data.
    - upload_statement(data): Uploads a bank statement to a storage service and saves the statement data in a repository.
    - upload_statements(user_id, company_records): Generates and uploads bank statements for multiple companies and branches.
    """
    """
        Generates a bank statement in CSV format based on the provided data.
        Parameters:
        - data (dict): The data required to generate the statement.
        Returns:
        - statement_file_path (str): The file path of the generated statement.
        Raises:
        - Exception: If there is an error generating the statement.
        """
    pass
    """
        Uploads a bank statement to a storage service and saves the statement data in a repository.
        Parameters:
        - data (dict): The data required to upload the statement.
        Raises:
        - Exception: If there is an error uploading the statement.
        """
    pass
    """
        Generates and uploads bank statements for multiple companies and branches.
        Parameters:
        - user_id (int): The ID of the user uploading the statements.
        - company_records (dict): A dictionary containing the company records.
        """
    pass

    @staticmethod
    def generate_statement(data):
        try:
            statement_file_path = Parser.generate_csv(data)
            return statement_file_path
        except Exception as e:
            raise Exception(f"Error generating statement: {str(e)}")

    @staticmethod
    def upload_statement(data):
        try:
            file_path = data['file_path']
            s3_url = S3Client.upload_file(file_path)
            data['statement_data'] = s3_url
            BankStatementRepository.save_statement(data, s3_url)
            statement_id = BankStatementRepository.get_statement_id(data)
            if statement_id:
                transactions = Parser.parse_csv(file_path)
                TransactionRepository.add_transactions(
                    transactions, statement_id, data['branch_id'])
            else:
                raise Exception("Failed to retrieve statement ID")
        except Exception as e:
            raise Exception(f"Error uploading statement: {str(e)}")

    @staticmethod
    def upload_statements(user_id, company_records):
        os.makedirs('generated_data', exist_ok=True)
        for company, details in company_records.items():
            company_id = details['company_id']
            for branch_name in details['branches']:
                branch = BranchRepository.get_branch_by_name_and_company(
                    branch_name, company_id)
                if not branch:
                    print(
                        f"Branch {branch_name} not found for company {company}")
                    continue

                data = generate_random_transactions(company, branch_name)
                print(f"Statement generated for {company} - {branch_name}")
                try:
                    statement = BankStatementService.generate_statement(data)

                    upload_data = {
                        "user_id": user_id,
                        "company_id": company_id,
                        "branch_id": branch.branch_id,
                        "statement_date": datetime.now().strftime('%Y-%m-%d'),
                        "file_path": statement
                    }
                    BankStatementService.upload_statement(upload_data)
                    print(f"Statement uploaded successfully for {
                          company} - {branch_name}")
                except Exception as e:
                    print(f"Error: {str(e)}")
