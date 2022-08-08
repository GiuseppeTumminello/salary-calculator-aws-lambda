import uuid
import boto3


def monthly_gross_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName='monthly_gross',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(event['amount'])},
                            'description': {'S': 'Monthly gross'}})
    return {'Monthly gross': event['amount']}
