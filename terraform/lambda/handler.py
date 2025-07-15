import os
import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

def lambda_handler(event, context):
    key = f"lambda-{datetime.utcnow().isoformat()}.txt"
    s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=b"Created by lambda")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "File created", "key": key})
    }
