import json
import uuid
import boto3

month = 12
sqs = boto3.client('sqs', region_name="us-east-1")
queue_url = sqs.get_queue_url(QueueName='salary-calculator-orchestrator-queue').get('QueueUrl')
dynamodb = boto3.client('dynamodb')
description = 'Annual gross'
table_name = 'annual_gross'
column = dynamodb.Table(table_name)


def annual_gross_handler(event, context):
    annual_gross = AnnualGross.calculate_annual_gross(event['amount'])
    Sqs.send_message_to_queue(annual_gross)
    DynamoDb.save_data(annual_gross)
    return {description: annual_gross}


class AnnualGross:
    def calculate_annual_gross(self):
        return self * month


class DynamoDb:
    def save_data(self):
        dynamodb.put_item(TableName=table_name,
                          Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(self)},
                                'description': {'S': description}})

class Sqs:
    def send_message_to_queue(self):
        message = {"amount": self}
        sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))
