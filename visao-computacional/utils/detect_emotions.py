import boto3

rekognition = boto3.client("rekognition")


def detect_emotions(bucket, image_name):
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket, 
                "Name": image_name
            }
        }, 
        Attributes=["ALL"]
    )

    return response
