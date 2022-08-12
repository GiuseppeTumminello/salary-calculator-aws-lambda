import boto3
import json

SQS = boto3.client('sqs')
SEND_MESSAGE_QUEUE_URL = SQS.get_queue_url(QueueName='salary-calculator-orchestrator-queue').get('QueueUrl')
RECEIVE_MESSAGE_QUEUE_URL = SQS.get_queue_url(QueueName='monthly-gross-queue').get('QueueUrl')


def read_message_from_queue():
    response = SQS.receive_message(
        QueueUrl=RECEIVE_MESSAGE_QUEUE_URL, AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=1, MessageAttributeNames=['All'], VisibilityTimeout=0, WaitTimeSeconds=0
    )
    message = json.loads(response['Messages'][0]['Body'])
    message_to_delete = response['Messages'][0]
    receipt_handle = message_to_delete['ReceiptHandle']
    SQS.delete_message(QueueUrl=RECEIVE_MESSAGE_QUEUE_URL, ReceiptHandle=receipt_handle)
    return message['Message']
