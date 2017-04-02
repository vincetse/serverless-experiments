import json

def get_uuid(event, context):
    import uuid
    n = 1
    if "n" in event["queryStringParameters"]:
        n = int(event["queryStringParameters"]["n"])
    uuids = []
    for i in xrange(n):
        uuids.append(str(uuid.uuid4()))
    body = {
        "uuid": uuids
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
