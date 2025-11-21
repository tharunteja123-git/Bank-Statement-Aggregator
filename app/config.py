import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for the application.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLAlchemy database.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag indicating whether to track modifications in the database.
        AWS_ACCESS_KEY (str): The access key for AWS.
        AWS_SECRET_KEY (str): The secret key for AWS.
        S3_BUCKET (str): The name of the S3 bucket.
    """
    '''SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    S3_BUCKET = os.getenv('S3_BUCKET')'''
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
    'SQLALCHEMY_DATABASE_URI',
    'mysql+pymysql://batch_user:batch_pass@localhost/batch74_db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Dummy values
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', 'test-access-key')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', 'test-secret-key')
    S3_BUCKET = os.getenv('S3_BUCKET', 'local-bucket')
