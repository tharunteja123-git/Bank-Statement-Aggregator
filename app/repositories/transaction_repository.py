import logging
from app.models.transaction import Transaction
from app.utils.db import db


class TransactionRepository:
    """
    Repository class for managing transactions.
    This class provides methods for adding and aggregating transactions.
    Methods:
    - add_transactions(transactions, statement_id, branch_id): Adds transactions to the database.
    - aggregate_transactions(transactions): Aggregates the total debits and credits from a list of transactions.
    """
    """
        Adds transactions to the database.
        Args:
        - transactions (list): A list of transactions to be added.
        - statement_id (int): The ID of the statement associated with the transactions.
        - branch_id (int): The ID of the branch associated with the transactions.
        Returns:
        None
        """
    # Add statement_id and branch_id to each transaction
    # Create a new Transaction object and add it to the session
    # Commit the changes to the database
    # Log a success message
    """
        Aggregates the total debits and credits from a list of transactions.
        Args:
        - transactions (list): A list of transactions to be aggregated.
        Returns:
        dict: A dictionary containing the total debits and credits.
        """
    # Calculate the total debits and credits
    # Return the aggregated results
    @staticmethod
    def add_transactions(transactions, statement_id, branch_id):
        for transaction in transactions:
            transaction['statement_id'] = statement_id
            transaction['branch_id'] = branch_id
            new_transaction = Transaction(**transaction)
            db.session.add(new_transaction)
        db.session.commit()
        logging.info("Transactions added successfully")

    @staticmethod
    def aggregate_transactions(transactions):
        total_debits = sum(t['amount']
                           for t in transactions if t['amount'] < 0)

        total_credits = sum(t['amount']
                            for t in transactions if t['amount'] > 0)

        return {
            'total_debits': total_debits,
            'total_credits': total_credits
        }
