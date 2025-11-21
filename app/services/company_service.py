from app.repositories.company_repository import CompanyRepository


class CompanyService:
    """
    Add a new company to the system.
    Args:
        data (dict): A dictionary containing the company data.
    Raises:
        Exception: If an error occurs while adding the company.
    """
    """
    Retrieve a list of all companies.
    Returns:
        list: A list of company objects.
    Raises:
        Exception: If an error occurs while retrieving the companies.
    """
    @staticmethod
    def add_company(data):
        try:
            CompanyRepository.add_company(data)
        except Exception as e:
            raise Exception(f"Error adding company: {str(e)}")

    @staticmethod
    def get_companies():
        try:
            companies = CompanyRepository.get_companies()
            return companies
        except Exception as e:
            raise Exception(f"Error retrieving companies: {str(e)}")
