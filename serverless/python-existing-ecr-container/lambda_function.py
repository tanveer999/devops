import json
# import requests

def hello(event, context):

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}