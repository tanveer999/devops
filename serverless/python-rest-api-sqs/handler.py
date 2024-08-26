import json
# import requests

def hello(event, context):
    # body = {
    #     "message": "Go Serverless v3.0! Your function executed successfully!",
    #     "input": event,
    # }
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}

# def get_dummy_data(event, context):
#     dummy_data = requests.get('https://catfact.ninja/fact')

#     response = {
#         "statusCode": dummy_data.status_code,
#         "body": dummy_data.text
#     }

#     return response

    # response = {
    #     "statusCode": res.status_code,
    #     "body": res.text
    # }