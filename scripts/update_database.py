import os
import csv
import sys
from datetime import datetime
from app.models.user import User
from app.models.company import Company
from app.models.branch import Branch
from app.models.bank_statement import BankStatement
from app.models.transaction import Transaction
from app.utils.db import db
from cryptography.fernet import Fernet

# Function to read a CSV file and return its contents as a list of dictionaries


def read_csv(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            transactions = [row for row in reader]
        return transactions
    except IOError:
        print(f"Error reading CSV file: {file_path}")
        return None

# Function to get or create a company in the database


def get_or_create_company(company_name):
    try:
        company = Company.query.filter_by(company_name=company_name).first()
        if not company:
            company = Company(company_name=company_name)
            db.session.add(company)
            db.session.commit()
        return company
    except Exception as e:
        print(f"Error creating or retrieving company: {e}")
        sys.exit(1)

# Function to get or create a branch in the database


def get_or_create_branch(branch_name, company_name, bank_name):
    try:
        company = get_or_create_company(company_name)
        if not company:
            return None
        branch = Branch.query.filter_by(
            branch_name=branch_name, company_id=company.company_id).first()
        if not branch:
            branch = Branch(branch_name=branch_name,
                            company_id=company.company_id, bank_name=bank_name)
            db.session.add(branch)
            db.session.commit()
        return branch
    except Exception as e:
        print(f"Error creating or retrieving branch: {e}")
        sys.exit(1)

# Function to save a user in the database


def save_user(transaction):
    try:
        company = get_or_create_company(transaction['company_name'])
        if not company:
            return None
        user = User.query.filter_by(email=transaction['user_id']).first()
        if not user:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            encrypted_email = cipher_suite.encrypt(
                transaction['user_id'].encode())
            encrypted_password = cipher_suite.encrypt('password'.encode())

            user = User(
                username=f"{transaction['company_name']}_user",
                email=encrypted_email,
                password=encrypted_password,
                company_id=company.company_id
            )
            db.session.add(user)
            db.session.commit()
        return user.user_id
    except Exception as e:
        print(f"Error saving user: {e}")
        return None

# Function to save a bank statement in the database


def save_bank_statement(transaction, user_id):
    try:
        company = get_or_create_company(transaction['company_name'])
        if not company:
            return None
        branch = get_or_create_branch(
            transaction['branch_name'], transaction['company_name'], transaction['bank_name'])
        if not branch:
            return None

        new_statement = BankStatement(
            user_id=user_id,
            company_id=company.company_id,
            branch_id=branch.branch_id,
            statement_date=datetime.now().strftime('%Y-%m-%d'),
            statement_data=f"s3://{transaction['company_name']
                                   }_{transaction['branch_name']}_transactions.csv"
        )
        db.session.add(new_statement)
        db.session.commit()
        return new_statement.statement_id
    except Exception as e:
        print(f"Error saving bank statement: {e}")
        return None

# Function to save transactions to the database


def save_transactions_to_db(transactions):
    try:
        for transaction in transactions:
            user_id = save_user(transaction)
            if not user_id:
                continue
            statement_id = save_bank_statement(transaction, user_id)
            if not statement_id:
                continue

            branch = get_or_create_branch(
                transaction['branch_name'], transaction['company_name'], transaction['bank_name'])
            if not branch:
                continue

            new_transaction = Transaction(
                statement_id=statement_id,
                date=datetime.strptime(transaction['date'], '%Y-%m-%d'),
                amount=float(transaction['amount']),
                description=transaction['description'],
                company_name=transaction['company_name'],
                branch_id=branch.branch_id
            )
            db.session.add(new_transaction)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error saving transactions to the database: {e}")
        return None

# Function to update the database with transactions from CSV files


def update():
    try:
        for root, dirs, files in os.walk('down_data'):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    transactions = read_csv(file_path)
                    if transactions is None:
                        continue
                    save_transactions_to_db(transactions)
        print("Transactions saved to the database")
    except Exception as e:
        print(f"Error updating database: {e}")
        sys.exit(1)
