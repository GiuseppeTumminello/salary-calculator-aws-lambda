import boto3
import json

SQS = boto3.client('sqs')
RECEIVE_MESSAGE_QUEUE_URL = SQS.get_queue_url(QueueName='salary-calculator-orchestrator-queue').get('QueueUrl')


def read_message_from_queue(response):
    message = json.loads(response['Records'][0]['body'])

    message_to_delete = response['Records'][0]
    receipt_handle = message_to_delete['receiptHandle']
    SQS.delete_message(QueueUrl=RECEIVE_MESSAGE_QUEUE_URL, ReceiptHandle=receipt_handle)

    return message
