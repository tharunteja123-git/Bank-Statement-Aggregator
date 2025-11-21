from app.models.bank_statement import BankStatement
from app.utils.db import db


class BankStatementRepository:
    """
    Repository class for managing bank statements.
    """
    """
        Saves a bank statement to the database.
        Args:
            data (dict): A dictionary containing the bank statement data.
                - user_id (int): The ID of the user associated with the statement.
                - company_id (int): The ID of the company associated with the statement.
                - branch_id (int): The ID of the branch associated with the statement.
                - statement_date (datetime): The date of the statement.
            s3_url (str): The URL of the statement data stored in Amazon S3.
        Returns:
            None
        """
    """
        Retrieves the ID of a bank statement from the database.
        Args:
            data (dict): A dictionary containing the bank statement data.
                - user_id (int): The ID of the user associated with the statement.
                - company_id (int): The ID of the company associated with the statement.
                - branch_id (int): The ID of the branch associated with the statement.
                - statement_date (datetime): The date of the statement.
                - statement_data (str): The URL of the statement data stored in Amazon S3.
        Returns:
            int or None: The ID of the statement if found, None otherwise.
        """
    @staticmethod
    def save_statement(data, s3_url):
        new_statement = BankStatement(
            user_id=data['user_id'],
            company_id=data['company_id'],
            branch_id=data['branch_id'],
            statement_date=data['statement_date'],
            statement_data=s3_url
        )
        db.session.add(new_statement)
        db.session.commit()

    @staticmethod
    def get_statement_id(data):
        statement = BankStatement.query.filter_by(
            user_id=data['user_id'],
            company_id=data['company_id'],
            branch_id=data['branch_id'],
            statement_date=data['statement_date'],
            statement_data=data['statement_data']
        ).first()
        return statement.statement_id if statement else None
