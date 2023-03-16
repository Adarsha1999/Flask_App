from flask import Flask
import boto3
import os
access_key = os.getenv('access_key')
secret_access_key = os.getenv("secret_access_key")
print(access_key,secret_access_key)
client = boto3.client('dynamodb',aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name="us-east-1")
app = Flask(__name__)
@app.route('/')
def hello():
    response = client.get_item(
    TableName='Candidates',
    Key={'CandidateName ':{'S':'atin'}}
    )
    return "Hello World"
if __name__ == "__main__":
    app.run()
