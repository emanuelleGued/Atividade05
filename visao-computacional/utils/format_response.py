from datetime import datetime


def format_response(emotions, bucket, image_name):
    faces = []

    for face in emotions["FaceDetails"]:
        primary_emotion = max(face["Emotions"], key=lambda x: x["Confidence"])

        face_data = {
            "position": {
                "Height": face["BoundingBox"]["Height"],
                "Left": face["BoundingBox"]["Left"],
                "Top": face["BoundingBox"]["Top"],
                "Width": face["BoundingBox"]["Width"],
            },
            "classified_emotion": primary_emotion["Type"],
            "classified_emotion_confidence": primary_emotion["Confidence"],
        }

        faces.append(face_data)

    if not faces:
        faces = [{
            "position": {
                "Height": None,
                "Left": None,
                "Top": None,
                "Width": None,
            },
            "classified_emotion": None,
            "classified_emotion_confidence": None,
        }]

    response = {
        "url_to_image": f"s3://{bucket}/{image_name}",
        "created_image": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "faces": faces,
    }

    return response
