import json

def lambda_handler(event, context):
    print("Received S3 event:", json.dumps(event))

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        event_name = record['eventName']

        print(f"Event Name: {event_name}")
        print(f"Bucket Name: {bucket_name}")
        print(f"Object Key: {object_key}")

        # You can add more processing here, e.g., download the object, analyze it, etc.
    return {
        'body': json.dumps('Successfully processed S3 event!')
    }
