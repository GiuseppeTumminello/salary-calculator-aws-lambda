import uuid

import boto3


session = boto3.Session(profile_name='Sandbox_Full-Administrator', region_name='us-east-1')
DYNAMODB = session.client('dynamodb')
DESCRIPTION = 'Annual gross'
TABLE_NAME = 'annual_gross'


class DynamoDb:
    def save_data(self):
        DYNAMODB.put_item(TableName=TABLE_NAME,
                          Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(self)},
                                'description': {'S': DESCRIPTION}})