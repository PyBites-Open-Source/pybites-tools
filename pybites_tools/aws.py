import argparse
import os
from typing import Optional

import boto3
from dotenv import load_dotenv

DEFAULT_BUCKET_PERMISSION = "public-read"

load_dotenv()


def upload_to_s3(
    filepath: str, bucket: Optional[str] = None, acl: Optional[str] = None
) -> str:
    s3_bucket = bucket or os.environ["AWS_S3_BUCKET"]
    acl = acl or DEFAULT_BUCKET_PERMISSION

    aws_key = os.environ["AWS_ACCESS_KEY_ID"]
    aws_secret = os.environ["AWS_SECRET_ACCESS_KEY"]
    aws_region = os.environ["AWS_REGION"]

    session = boto3.Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
    s3 = session.resource("s3")
    response = s3.Bucket(s3_bucket).put_object(
        Key=os.path.basename(filepath), Body=open(filepath, "rb"), ACL=acl
    )

    s3_file_link = f"https://{s3_bucket}.s3.{aws_region}.amazonaws.com/{response.key}"
    print(s3_file_link)

    return s3_file_link


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-b", "--bucket")
    parser.add_argument("-a", "--acl")

    args = parser.parse_args()
    upload_to_s3(args.file, args.bucket, args.acl)


if __name__ == "__main__":
    main()
