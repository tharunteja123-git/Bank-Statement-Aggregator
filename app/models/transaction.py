from app.utils.db import db


class Transaction(db.Model):
    """
    Represents a transaction in the bank statement aggregator.

    Attributes:
        transaction_id (int): The unique identifier of the transaction.
        statement_id (int): The foreign key referencing the bank statement to which the transaction belongs.
        date (date): The date of the transaction.
        amount (float): The amount of the transaction.
        description (str): The description of the transaction.
        company_name (str): The name of the company associated with the transaction.
        branch_id (int): The foreign key referencing the branch where the transaction occurred.
        branch (Branch): The branch object representing the branch where the transaction occurred.

    """
    __tablename__ = 'transaction'
    transaction_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    statement_id = db.Column(db.Integer, db.ForeignKey(
        'bank_statement.statement_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey(
        'branch.branch_id'), nullable=False)
    branch = db.relationship(
        'Branch', backref=db.backref('transactions', lazy=True))
