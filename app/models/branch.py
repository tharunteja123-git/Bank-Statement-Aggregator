from app.utils.db import db


class Branch(db.Model):
    """
    Represents a branch in a bank.
    Attributes:
        branch_id (int): The unique identifier of the branch.
        branch_name (str): The name of the branch.
        company_id (int): The unique identifier of the company that the branch belongs to.
        bank_name (str): The name of the bank.
    Methods:
        to_dict(): Returns a dictionary representation of the branch object.
    """
    """
        Returns a dictionary representation of the branch object.
        Returns:
            dict: A dictionary containing the branch information.
        """
    __tablename__ = 'branch'
    branch_id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(100), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company.company_id'), nullable=False)
    bank_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'branch_id': self.branch_id,
            'branch_name': self.branch_name,
            'company_id': self.company_id,
            'bank_name': self.bank_name
        }
