import boto3
import json
import os

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    BUCKET_NAME_FRONT = os.environ['BUCKET_NAME_FRONT']

    session = boto3.session.Session()
    region_name = session.region_name

    bucket_name = BUCKET_NAME_FRONT + '-' + region_name
    print('bucket_name', bucket_name)

    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)

    object_count = len([True for _ in bucket.objects.all()])
    print('object_count', object_count)

    for object in bucket.objects.all():
        print('\t', object.key)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
