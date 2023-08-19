import os
import boto3
from tqdm import tqdm

# Replace these with your AWS credentials
aws_access_key_id = 'AKIA4B7Z6CIDZAZCC2NU'
aws_secret_access_key = '7SpaDXqviwb9VntF822y3qAcTpCTA7Fb/zDspTs+'

# Replace this with your S3 bucket name
bucket_name = 'ext-candidate-data'

# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# List all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Iterate through objects and download files into corresponding local directories
for obj in tqdm(response.get('Contents', [])):
    object_key = obj['Key']

    # Skip directory objects (prefixes)
    if object_key.endswith('/'):
        continue

    local_path = os.path.dirname(object_key)
    local_filename = os.path.basename(object_key)

    # Create the local directory if it doesn't exist
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    # Download the object into the local directory
    local_file_path = os.path.join(local_path, local_filename)
    s3.download_file(bucket_name, object_key, local_file_path)

    print(f"Downloaded: {object_key} to {local_file_path}")

print("All objects downloaded.")
