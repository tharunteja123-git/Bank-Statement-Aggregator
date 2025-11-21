import os
import sys
from app.utils.s3 import S3Client


def upload():
    """
    Uploads all CSV files in the 'gen_data' directory to Amazon S3.

    This function creates the 'gen_data' directory if it doesn't exist and walks through all the files in the directory.
    It uploads each file with a '.csv' extension to Amazon S3 using the S3Client.upload_file() method.
    If the upload is successful, it prints the file name and the S3 URL. If there is an error during the upload,
    it prints the file name and the error message.

    Raises:
        Exception: If there is an error creating the 'gen_data' directory.

    Returns:
        None
    """
    while True:
        try:
            os.makedirs('gen_data', exist_ok=True)
            for root, dirs, files in os.walk('gen_data'):
                for file in files:
                    if file.endswith('.csv'):
                        file_path = os.path.join(root, file)
                        try:
                            s3_url = S3Client.upload_file(file_path)
                            print(f'Uploaded {file} to S3: {s3_url}')
                        except Exception as e:
                            print(f'Error uploading {file} to S3: {str(e)}')
                            sys.exit(1)
            print('All files uploaded to S3')
            break
        except Exception as e:
            print(f'Error creating directory: {str(e)}')
            print('Please try again.')
