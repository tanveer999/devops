import json
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    log.info('event:')
    log.info(event)
    log.info('context:')
    log.info(context)

    return {"statusCode": 200, "body": json.dumps(body)}
