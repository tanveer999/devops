import json
import sys
# import requests

def handler(event, context):

    body = {
        "message": f"1 Go Serverless v3.0! Your function executed successfully! and runtime is {sys.version}"
    }

    return {"statusCode": 200, "body": json.dumps(body)}