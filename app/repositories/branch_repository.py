from app.models.branch import Branch
from app.utils.db import db


class BranchRepository:
    """
    Repository class for managing branches in the application.
    Methods:
    - add_branch(data): Adds a new branch to the database.
    - get_branches(): Retrieves all branches from the database.
    - get_branch_by_name_and_company(branch_name, company_id): Retrieves a branch by its name and company ID.
    - get_default_branch_for_company(company_id): Retrieves the default branch for a given company ID.
    """
    """
        Adds a new branch to the database.
        Parameters:
        - data (dict): A dictionary containing the branch data.
        Returns:
        None
        """
    pass
    """
        Retrieves all branches from the database.
        Returns:
        list: A list of dictionaries representing the branches.
        """
    pass
    """
        Retrieves a branch by its name and company ID.
        Parameters:
        - branch_name (str): The name of the branch.
        - company_id (int): The ID of the company.
        Returns:
        Branch: The branch object matching the given name and company ID, or None if not found.
        """
    pass
    """
        Retrieves the default branch for a given company ID.
        Parameters:
        - company_id (int): The ID of the company.
        Returns:
        Branch: The default branch object for the given company ID, or None if not found.
        """
    pass

    @staticmethod
    def add_branch(data):
        new_branch = Branch(**data)
        db.session.add(new_branch)
        db.session.commit()

    @staticmethod
    def get_branches():
        branches = Branch.query.all()
        return [branch.to_dict() for branch in branches]

    @staticmethod
    def get_branch_by_name_and_company(branch_name, company_id):
        return Branch.query.filter_by(branch_name=branch_name, company_id=company_id).first()

    @staticmethod
    def get_default_branch_for_company(company_id):
        return Branch.query.filter_by(company_id=company_id).first()
