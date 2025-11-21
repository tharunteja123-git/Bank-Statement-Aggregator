from app.models.company import Company


class CompanyRepository:
    """
    Repository class for managing company data.

    This class provides methods to interact with the company data in the database.

    Attributes:
        None

    Methods:
        get_company_by_name: Retrieves a company from the database based on its name.

    """

    """
        Retrieves a company from the database based on its name.

        Args:
            company_name (str): The name of the company to retrieve.

        Returns:
            Company: The company object if found, None otherwise.

        """
    @staticmethod
    def get_company_by_name(company_name):
        return Company.query.filter_by(company_name=company_name).first()
