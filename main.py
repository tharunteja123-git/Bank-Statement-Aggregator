
'''from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Example route (homepage)
@app.route("/")
def home():
    return "🏦 Bank Statement Aggregator is running!"

# Run the app
if __name__ == "__main__":
    # debug=True enables auto-reload on code changes
    app.run(debug=True)'''

from app import create_app
"""
This script is the main entry point for the Bank Statement Aggregator application.
It imports necessary modules and defines the main function to run the application.
The application performs the following steps:
1. Generates transactions using the 'generate_transactions' script.
2. Uploads the generated transactions to an S3 bucket using the 'upload_to_s3' script.
3. Downloads transactions from the S3 bucket using the 'download_from_s3' script.
4. Updates the database with the downloaded transactions using the 'update_database' script.
5. Aggregates the statements using the 'aggregate_statements' script.
Usage:
    - Run this script to start the Bank Statement Aggregator application.
Note:
    - Make sure to configure the necessary settings in the 'app' module before running this script.
"""

from scripts.generate_transactions import generate
from scripts.upload_to_s3 import upload
from scripts.download_from_s3 import download
from scripts.update_database import update
from scripts.aggregate_statements import aggregate

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        generate()
        upload()
        download()
        update()
        aggregate()
    app.run()
