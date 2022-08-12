import uuid

import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Monthly gross'
TABLE_NAME = 'monthly_gross'


def save_data(monthly_gross, sns_uuid):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(monthly_gross)},
                            'description': {'S': DESCRIPTION}, 'uuid': {'S': str(sns_uuid)}})
