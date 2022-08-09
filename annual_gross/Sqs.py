import json
import boto3

session = boto3.Session(profile_name='Sandbox_Full-Administrator', region_name='us-east-1')
SQS = session.client('sqs', region_name="us-east-1")
SEND_MESSAGE_QUEUE_URL = SQS.get_queue_url(QueueName='salary-calculator-orchestrator-queue').get('QueueUrl')
RECEIVE_MESSAGE_QUEUE_URL = SQS.get_queue_url(QueueName='annual-gross-queue').get('QueueUrl')


class Sqs:

    def send_message_to_queue(self):
        message = self
        print(message)
        SQS.send_message(QueueUrl=SEND_MESSAGE_QUEUE_URL, MessageBody=str(message))

    @staticmethod
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
