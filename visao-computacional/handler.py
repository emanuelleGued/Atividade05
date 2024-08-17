import json
from utils.detect_emotions import detect_emotions
from utils.format_response import format_response


def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def v1_description(event, context):
    body = {"message": "VISION api version 1."}

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def v2_description(event, context):
    body = {"message": "VISION api version 2."}

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def v1_vision(event, context):
    try:
        body = json.loads(event["body"])
        bucket = body["bucket"]
        image_name = body["imageName"]

        emotions = detect_emotions(bucket, image_name)
        response = format_response(emotions, bucket, image_name)

        return {"statusCode": 200, "body": json.dumps(response)}

    except Exception as e:
        response = {"statusCode": 500, "body": json.dumps({"error": str(e)})}

        return response


def v2_vision(event, context):
    body = {"message": "VISION api version 2."}

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
