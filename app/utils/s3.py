import os
import boto3
from app.config import Config
import shutil


class S3Client:
    """
    A class that provides methods for uploading and downloading files to/from Amazon S3.
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
    pass
    """
        Downloads files from the specified S3 bucket.
        Args:
            data (dict): A dictionary containing the keys of the files to be downloaded.
        Returns:
            list: A list of file paths of the downloaded files.
        """
    pass
    s3 = boto3.client('s3',
                      aws_access_key_id=Config.AWS_ACCESS_KEY,
                      aws_secret_access_key=Config.AWS_SECRET_KEY)

    '''@staticmethod
    def upload_file(file_path):
        file_name = os.path.basename(file_path)
        S3Client.s3.upload_file(file_path, Config.S3_BUCKET, file_name)
        S3Client.s3.upload_file(file_path, Config.S3_BUCKET, file_name)
        return f"s3://{Config.S3_BUCKET}/{file_name}"'''
    
    @staticmethod
    def upload_file(file_path):
        file_name = os.path.basename(file_path)
        # Create the simulated "S3 bucket" folder
        local_bucket_path = os.path.join("local_s3", Config.S3_BUCKET)
        os.makedirs(local_bucket_path, exist_ok=True)
        
        # Define destination path
        destination = os.path.join(local_bucket_path, file_name)
        
        # Copy the file to simulate upload
        shutil.copy(file_path, destination)
        
        print(f"Simulated upload to {destination}\n")
        return f"local-s3://{Config.S3_BUCKET}/{file_name}"

    @staticmethod
    def download_files(data):
        if os.path.exists('down_data'):
            file_list = os.listdir('down_data')
            for file in file_list:
                file_path = os.path.join('down_data', file)
                os.remove(file_path)
        else:
            os.makedirs('down_data', exist_ok=True)
        files = []
        for key in data['keys']:
            file_path = os.path.join('down_data', os.path.basename(key))
            S3Client.s3.download_file(Config.S3_BUCKET, key, file_path)
            files.append(file_path)
        return files
