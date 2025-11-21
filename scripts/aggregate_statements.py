import csv
import os
import sys
from app.utils.db import db
from app.models.transaction import Transaction
from app.models.branch import Branch


def get_transactions_for_company(company_name, year, month):
    try:
        transactions = db.session.query(Transaction, Branch).join(Branch, Transaction.branch_id == Branch.branch_id).filter(
            Transaction.company_name == company_name,
            Transaction.date >= f"{year}-{month:02d}-01",
            Transaction.date < f"{
                year}-{month+1:02d}-01" if month < 12 else f"{year+1}-01-01"
        ).all()
        return transactions
    except Exception as e:
        print(f"Error retrieving transactions: {e}")
        return None


def aggregate_and_save(transactions, company_name):
    try:
        total_debits = sum(
            t.Transaction.amount for t in transactions if t.Transaction.amount < 0)
        total_credits = sum(
            t.Transaction.amount for t in transactions if t.Transaction.amount > 0)
        filename = f'aggr_data/{company_name}_aggregated.csv'

        os.makedirs('aggr_data', exist_ok=True)
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['transaction_id', 'statement_id', 'date', 'amount',
                          'description', 'company_name', 'branch_id', 'branch_name', 'bank_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction, branch in transactions:
                writer.writerow({
                    'transaction_id': transaction.transaction_id,
                    'statement_id': transaction.statement_id,
                    'date': transaction.date,
                    'amount': transaction.amount,
                    'description': transaction.description,
                    'company_name': transaction.company_name,
                    'branch_id': transaction.branch_id,
                    'branch_name': branch.branch_name,
                    'bank_name': branch.bank_name
                })
            writer.writerow({'transaction_id': 'Total Debits:', 'statement_id': '', 'date': '', 'amount': total_debits, 'description': '',
                             'company_name': '', 'branch_id': '', 'branch_name': '', 'bank_name': ''})
            writer.writerow({'transaction_id': 'Total Credits:', 'statement_id': '', 'date': '', 'amount': total_credits, 'description': '',
                             'company_name': '', 'branch_id': '', 'branch_name': '', 'bank_name': ''})
        print(f'Aggregated data saved to {filename}')
        print(f'Total debits: {total_debits}')
        print(f'Total credits: {total_credits}')
    except Exception as e:
        print(f"Error aggregating and saving data: {e}")
        sys.exit(1)


def aggregate():
    while True:
        try:
            # Read year and month from the temporary file
            try:
                with open('temp_config.txt', 'r') as f:
                    year, month = f.read().split(',')
                    year = int(year)
                    month = int(month)
            except FileNotFoundError:
                print(
                    "Temporary configuration file not found. Please run the download script first.")
                sys.exit(1)

            print("Select a company:")
            print("1. Apple_India")
            print("2. Apple_US")
            print("3. Google_India")
            print("4. Google_US")
            company_options = {
                1: 'Apple_India',
                2: 'Apple_US',
                3: 'Google_India',
                4: 'Google_US'
            }
            choice = int(
                input("Enter the number corresponding to the company: "))
            company_name = company_options.get(choice)
            if company_name:
                transactions = get_transactions_for_company(
                    company_name, year, month)
                aggregate_and_save(transactions, company_name)
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print(f"Error in aggregation process: {e}")
            sys.exit(1)
