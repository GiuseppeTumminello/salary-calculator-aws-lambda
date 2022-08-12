import json
import boto3

ARN = 'arn:aws:sns:us-east-1:342003767516:salary-calculator-topic'

sns = boto3.client('sns')


def publish_message_to_sns(message):
    sns.publish(
        TargetArn=ARN,
        Message=json.dumps({'default': str(message)}),
        MessageStructure='json'
    )
