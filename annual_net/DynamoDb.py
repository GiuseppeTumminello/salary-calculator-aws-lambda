import uuid

import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Annual gross'
TABLE_NAME = 'annual_net'


class DynamoDb:
    def save_data(self):
        DYNAMODB.put_item(TableName=TABLE_NAME,
                          Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(self)},
                                'description': {'S': DESCRIPTION}})
