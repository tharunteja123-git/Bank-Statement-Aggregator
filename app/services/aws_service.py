import os
import boto3
from app.config import Config


class S3Client:
    """
    A class that provides methods for interacting with AWS S3.
    Attributes:
        s3: An instance of the boto3 S3 client.
    Methods:
        upload_file(file_path): Uploads a file to the specified S3 bucket.
        download_files(data): Downloads files from the specified S3 bucket.
    """
    """
        Uploads a file to the specified S3 bucket.
        Args:
            file_path (str): The path of the file to be uploaded.
        Returns:
            str: The S3 URL of the uploaded file.
        """
    """
        Downloads files from the specified S3 bucket.
        Args:
            data (dict): A dictionary containing the keys of the files to be downloaded.
        Returns:
            list: A list of file paths of the downloaded files.
        """
    s3 = boto3.client('s3',
                      aws_access_key_id=Config.AWS_ACCESS_KEY,
                      aws_secret_access_key=Config.AWS_SECRET_KEY)

    @staticmethod
    def upload_file(file_path):
        file_name = os.path.basename(file_path)
        S3Client.s3.upload_file(file_path, Config.S3_BUCKET, file_name)
        return f"s3://{Config.S3_BUCKET}/{file_name}"

    @staticmethod
    def download_files(data):
        os.makedirs('downloaded_data', exist_ok=True)
        files = []
        for key in data['keys']:
            file_path = os.path.join('downloaded_data', os.path.basename(key))
            S3Client.s3.download_file(Config.S3_BUCKET, key, file_path)
            files.append(file_path)
        return files
