import json
import uuid
import boto3

month = 12
sqs = boto3.client('sqs', region_name="us-east-1")
queue_url = sqs.get_queue_url(QueueName='salary-calculator-orchestrator-queue').get('QueueUrl')


def send_message_to_queue(self):
    message = {"amount": self}
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))


def annual_gross_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    annual_gross = event['amount'] * month
    send_message_to_queue(annual_gross)
    dynamodb.put_item(TableName='annual_gross',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(annual_gross)},
                            'description': {'S': 'Annual gross'}})
    return {'Annual gross': annual_gross}
