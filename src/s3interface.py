import os
import boto3
from datetime import datetime
from credentials import *

#Format time for use in filename
now = datetime.now()  # current date and time
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%d-%m-%Y - %H:%M:%S")

# RUN TIME VARIABLES
s3Key = f'scraper test {date_time}.txt'
readWrite = "read"  # options are write or read
# END OF RUNTIME VARIABLES




bucket = "scrapertestbucket"
session = boto3.Session(aws_access_key_id=accessID, aws_secret_access_key=accessKey)
s3 = session.client('s3', region_name="eu-west-1")

def putS3(tidy_prices):
    global bucket
    global s3Key
    global s3

    """Converts list to .txt file to allow easy upload"""
    with open('prices-file.txt', 'w') as f:
        for item in tidy_prices:
            f.write("%s\n" % item)

    s3.upload_file('prices-file.txt', Bucket=bucket, Key=s3Key)
    if os.path.exists("prices-file.txt"):
        os.remove("prices-file.txt")

