import csv
import os
import random
from datetime import datetime, timedelta
import calendar
import sys


def generate_random_transactions(company_name, branch_name, branch_id, bank_name, statement_id, user_id, company_id, month, year, num_transactions=100):
    transactions = []
    days_in_month = calendar.monthrange(year, month)[1]
    start_date = datetime(year, month, 1)
    end_date = datetime(year, month, days_in_month)

    for i in range(num_transactions):
        transaction_date = start_date + \
            timedelta(days=random.randint(0, (end_date - start_date).days))
        transaction = {
            'transaction_id': i + 1,
            'statement_id': statement_id,
            'date': transaction_date.strftime('%Y-%m-%d'),
            'amount': round(random.uniform(-1000, 1000), 2),
            'description': f'Transaction {i + 1}',
            'company_name': company_name,
            'branch_name': branch_name,
            'branch_id': branch_id,
            'bank_name': bank_name,
            'user_id': user_id,
            'company_id': company_id
        }
        transactions.append(transaction)
    return transactions


def save_transactions_to_csv(transactions, filename):
    os.makedirs('gen_data', exist_ok=True)
    file_path = os.path.join('gen_data', filename)
    try:
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['transaction_id', 'statement_id', 'date', 'amount', 'description',
                          'company_name', 'branch_name', 'branch_id', 'bank_name', 'user_id', 'company_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except IOError:
        print(f"Error: Failed to write transactions to {filename}")
        sys.exit(1)


def get_month_year_selection():
    current_year = datetime.now().year
    previous_years = list(range(2000, current_year + 1))
    month_names = list(calendar.month_name)[1:]

    while True:
        print("Select a month:")
        for i, month in enumerate(month_names):
            print(f"{i+1}. {month}")

        try:
            month_selection = int(input("Enter the number of the month: "))
            if month_selection < 1 or month_selection > 12:
                raise ValueError("Invalid month selection")
            break
        except ValueError:
            print("Error: Invalid month selection")

    while True:
        print("Select a year:")
        for i, year in enumerate(previous_years):
            print(f"{i+1}. {year}")

        try:
            year_selection = int(input("Enter the number of the year: "))
            if year_selection < 1 or year_selection > len(previous_years):
                raise ValueError("Invalid year selection")
            break
        except ValueError:
            print("Error: Invalid year selection")

    return month_selection, previous_years[year_selection - 1]


def generate():
    """
    Generates bank statements for multiple companies and branches based on the given month and year selection.
    Returns:
        None
    """
    try:
        # Define the companies and their details
        companies = {
            'Apple_India': {'branches': [('Hyderabad', 1), ('Mumbai', 2), ('Bangalore', 3)], 'bank_name': 'SBI', 'user_id': 1, 'company_id': 1},
            'Apple_US': {'branches': [('New York', 4), ('San Francisco', 5), ('Los Angeles', 6)], 'bank_name': 'Chase', 'user_id': 2, 'company_id': 2},

            'Google_India': {'branches': [('Bangalore', 7), ('Delhi', 8), ('Pune', 9)], 'bank_name': 'ICICI', 'user_id': 3, 'company_id': 3},
            'Google_US': {'branches': [('Mountain View', 10), ('Seattle', 11), ('Austin', 12)], 'bank_name': 'DBS', 'user_id': 4, 'company_id': 4}
        }

        # Get the month and year selection from the user
        while True:
            month, year = get_month_year_selection()

            # If month or year is not provided, ask again
            if month is None or year is None:
                continue

            # Generate transactions for each company and branch
            for company, details in companies.items():
                for branch_name, branch_id in details['branches']:
                    statement_id = branch_id
                    transactions = generate_random_transactions(
                        company, branch_name, branch_id, details['bank_name'], statement_id, details['user_id'], details['company_id'], month, year)
                    filename = f'{company}_{branch_name}_{
                        year}_{month:02d}.csv'
                    save_transactions_to_csv(transactions, filename)
                    print(f'Statement generated for {company} - {branch_name}')
            break
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
