from app.utils.db import db


class BankStatement(db.Model):
    """
    Represents a bank statement.

    Attributes:
        statement_id (int): The unique identifier of the bank statement.
        user_id (int): The user ID associated with the bank statement.
        company_id (int): The company ID associated with the bank statement.
        branch_id (int): The branch ID associated with the bank statement.
        statement_date (Date): The date of the bank statement.
        statement_data (str): The data of the bank statement.
        transactions (list of Transaction): The transactions associated with the bank statement.

    """

    __tablename__ = 'bank_statement'
    statement_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company.company_id'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey(
        'branch.branch_id'), nullable=False)
    statement_date = db.Column(db.Date, nullable=False)
    statement_data = db.Column(db.String(255), nullable=False)
    transactions = db.relationship(
        'Transaction', backref='statement', lazy=True)
