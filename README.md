# Bank Statement Aggregator

## Project Overview

The Bank Statement Aggregator is a comprehensive system designed to manage and process bank statements for multiple companies and their branches. This project includes functionalities for generating, uploading, downloading, and updating bank statements, as well as aggregating data for analysis.

## Prerequisites

- Python 3.12
- MySQL
- AWS Account with S3 Bucket
- Required Python packages (listed in `requirements.txt`)

## Project Structure

```
BSA
├── app
│   ├── controllers
│   │   ├── __init__.py 
│   │   ├── branch_controller.py
│   │   ├── company_controller.py
│   │   ├── statement_controller.py
│   │   └── user_controller.py
│   ├── models
│   │   ├── bank_statement.py
│   │   ├── branch.py
│   │   ├── company.py
│   │   ├── transaction.py
│   │   └── user.py
│   ├── repositories
│   │   ├── bank_statement_repository.py
│   │   ├── branch_repository.py
│   │   ├── company_repository.py
│   │   ├── transaction_repository.py
│   │   └── user_repository.py
│   ├── services
│   │   ├── aws_service.py
│   │   ├── bank_statement_service.py
│   │   ├── branch_service.py
│   │   ├── company_service.py
│   │   └── user_service.py
│   ├── utils
│   │   ├── db.py
│   │   ├── parser.py
│   │   └── s3.py
│   ├── __init__.py 
│   └── config.py 
├── migrations
│   ├── 001_create_company_table.sql
│   ├── 002_create_branch_table.sql
│   ├── 003_create_user_table.sql
│   ├── 004_create_bank_statement_table.sql
│   └── 005_create_transaction_table.sql
├── scripts
│   ├── aggregate_statements.py
│   ├── download_from_s3.py
│   ├── generate_transactions.py
│   ├── update_database.py
│   └── upload_to_s3.py
├── .gitignore
├── erd.png
├── LICENSE
├── main.py
├── README.md  
└── requirements.txt
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tharunteja123-git/Bank-Statement-Aggregator
   cd BSA
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**

   ```bash
   cd migrations
   mysql -u [your_username] -p
   [your_password]
   create database [your_database];   
   source 001_create_company_table.sql
   source 002_create_branch_table.sql
   source 003_create_user_table.sql
   source 004_create_bank_statement_table.sql
   source 005_create_transaction_table.sql
   ```

5. **Configure AWS S3**

   Ensure you have AWS credentials set up with access to the S3 bucket. Under the bucket settings in the Permissions section, uncheck all the options for blocking all public access, and then copy and paste the policy code below into the bucket policy.

   ```json
   {
      "Version": "2012-10-17",
      "Statement": [
         {
               "Effect": "Allow",
               "Principal": "*",
               "Action": "s3:ListBucket",
               "Resource": "arn:aws:s3:::[bucket_name]"
         },
         {
               "Effect": "Allow",
               "Principal": "*",
               "Action": [
                  "s3:PutObject",
                  "s3:GetObject"
               ],
               "Resource": "arn:aws:s3:::[bucket_name]/*"
         }
      ]
   }
   ```

6. **Run The Application**

   ```bash
   python main.py
   ```

## Sample Transaction Data

Below is a snippet of the generated transaction records (CSV format):

```csv
transaction_id,statement_id,date,amount,description,company_name,branch_name,branch_id,bank_name,user_id,company_id
1,3,2000-01-02,-812.59,Transaction 1,Apple_India,Bangalore,3,SBI,1,1
2,3,2000-01-10,-169.26,Transaction 2,Apple_India,Bangalore,3,SBI,1,1
3,3,2000-01-14,-233.76,Transaction 3,Apple_India,Bangalore,3,SBI,1,1
4,3,2000-01-18,333.49,Transaction 4,Apple_India,Bangalore,3,SBI,1,1
5,3,2000-01-06,541.19,Transaction 5,Apple_India,Bangalore,3,SBI,1,1
100,3,2000-01-21,-58.2,Transaction 100,Apple_India,Bangalore,3,SBI,1,1


**Technologies Used:**
Programming Language: Python 3.12

Framework: Flask (for app context and modular structure)

Database: MySQL (with SQLAlchemy ORM for CRUD operations)

Cloud Storage: AWS S3 (for uploading and downloading CSV files)

Encryption: Python libraries for securing sensitive user data

Version Control: Git & GitHub (for collaboration and repo management)

Environment Management: Virtualenv (venv/.venv)

Utilities:

boto3 → AWS S3 integration

pandas → CSV parsing and aggregation

mysql-connector / SQLAlchemy → Database connectivity

Documentation & Diagrams: README.md, ERD (erd.png)

## Backend Workflow

1. **Data Generation** 

   1. Generate random transactions for specified companies and branches.
   2. Save generated transactions to CSV files in a local directory.

2. **File Upload**

   1. Upload the generated CSV files from the local directory to AWS S3.

3. **Data Retrieval and Aggregation**

   1. Retrieve transactions for a specified company, year, and month from the database.
   2. Aggregate the transaction data and save the results to a CSV file.

4. **Data Encryption**

   1. Encrypt sensitive user information before storing it in the database.

5. **Database Management**

   1. Manage and perform CRUD operations on various entities (users, companies, branches, transactions) using SQLAlchemy.


## Contributors
- **[Tharun Teja Nudagala](https://www.linkedin.com/in/tharun-teja-nudagala-11b2a7290)** - Code and logic


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

I would like to extend my sincere gratitude to [Srujana](https://www.linkedin.com/in/srujanavattamwar/) for their invaluable support. Their patience and belief in my abilities were instrumental in the successful completion of this work.