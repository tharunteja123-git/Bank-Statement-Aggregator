from app.repositories.branch_repository import BranchRepository


class BranchService:
    """
    Add a new branch to the system.
    Args:
        data (dict): A dictionary containing the branch data.
    Raises:
        Exception: If an error occurs while adding the branch.
    """
    """
    Retrieve all branches from the system.
    Returns:
        list: A list of branches.
    Raises:
        Exception: If an error occurs while retrieving the branches.
    """
    @staticmethod
    def add_branch(data):
        try:
            BranchRepository.add_branch(data)
        except Exception as e:
            raise Exception(f"Error adding branch: {str(e)}")

    @staticmethod
    def get_branches():
        try:
            branches = BranchRepository.get_branches()
            return branches
        except Exception as e:
            raise Exception(f"Error retrieving branches: {str(e)}")
