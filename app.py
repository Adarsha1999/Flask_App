from flask import Flask
import boto3
import os
access_key = os.getenv('access_key')
secret_access_key = os.getenv("secret_access_key")
print(access_key,secret_access_key)
dynamodb = boto3.resource('dynamodb',aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name="us-east-1")
app = Flask(__name__)
@app.route('/')
def hello():
    table = dynamodb.Table('Candidates')
    response = table.get_item(Key={'CandidateName': "atin"})
    item = response['Item']
    print(item)

    return "Hello World"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
