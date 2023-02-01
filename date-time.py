#!/usr/bin/env python3.9

from datetime import date
import time
import sys
import boto3
import os

#s3_bucket = os.environ.get("S3_BUCKET")
#s3 = boto3.client('s3',
#        region_name="us-east-1",
#        aws_access_key_id=os.environ.get("AWS_KEY"),
#        aws_secret_access_key=os.environ.get("AWS_SECRET_KEY")
#    )

AWS_KEY_ID = os.environ.get("AWS_KEY")
AWS_KEY_VALUE = os.environ.get("AWS_SECRET_KEY")

print(AWS_KEY_ID)
print(AWS_KEY_VALUE)
#session = boto3.Session(
#    aws_access_key_id=AWS_KEY_ID,
#    aws_secret_access_key=AWS_KEY_VALUE,
#)

s3 = boto3.resource('s3')

today = date.today()
time = (time.strftime("%I:%M:%S"))

sys.stdout = open('CreationTime', 'w')
print("Container was Assimilated at ", today, "at", time)
sys.stdout.close()

with open('./CreationTime', 'rb') as data:
    response = s3.Object("karmada.fwtest1.com", "Creation/NGINX").get()
    print(response['Body'].read())
    print(data)
