import csv
import os


class Parser:
    """
    Utility class for generating and parsing CSV files.
    Methods:
    - generate_csv(data): Generates a CSV file with the provided data.
    - parse_csv(file_path): Parses a CSV file and returns a list of transactions.
    """
    """
        Generates a CSV file with the provided data.
        Args:
        - data (dict): A dictionary containing the data for generating the CSV file.
          - company_name (str): The name of the company.
          - branch_name (str): The name of the branch.
          - date (str): The date in the format 'YYYY-MM-DD'.
          - transactions (list): A list of transaction dictionaries.
            Each transaction dictionary should contain the following keys:
            - date (str): The date of the transaction.
            - amount (float): The amount of the transaction.
            - description (str): The description of the transaction.
        Returns:
        - file_path (str): The file path of the generated CSV file.
        """
    """
        Parses a CSV file and returns a list of transactions.
        Args:
        - file_path (str): The file path of the CSV file to be parsed.
        Returns:
        - transactions (list): A list of transaction dictionaries.
          Each transaction dictionary contains the following keys:
          - date (str): The date of the transaction.
          - amount (float): The amount of the transaction.
          - description (str): The description of the transaction.
          - company_name (str): The name of the company.
        """
    @staticmethod
    def generate_csv(data):
        os.makedirs('generated_data', exist_ok=True)
        file_name = f"{data['company_name']}_{data['branch_name']}_{
            data['date'].replace('-', '')}.csv"
        file_path = os.path.join('generated_data', file_name)
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'amount', 'description', 'company_name'])
            for transaction in data['transactions']:
                writer.writerow([
                    transaction['date'],
                    transaction['amount'],
                    transaction['description'],
                    data['company_name']
                ])
        return file_path

    @staticmethod
    def parse_csv(file_path):
        transactions = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({
                    'date': row['date'],
                    'amount': float(row['amount']),
                    'description': row['description'],
                    'company_name': row['company_name']
                })
        return transactions
