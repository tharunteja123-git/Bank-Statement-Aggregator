from app.utils.db import db


class Company(db.Model):
    """
    Represents a company in the system.
    Attributes:
        company_id (int): The unique identifier of the company.
        company_name (str): The name of the company.
    Methods:
        to_dict(): Returns a dictionary representation of the company object.
    """
    """
        Returns a dictionary representation of the company object.
        Returns:
            dict: A dictionary containing the company_id and company_name.
        """
    __tablename__ = 'company'
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'company_id': self.company_id,
            'company_name': self.company_name
        }
