import uuid

import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Health'
TABLE_NAME = 'health'


def save_data(health):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(health)},
                            'description': {'S': DESCRIPTION}})
