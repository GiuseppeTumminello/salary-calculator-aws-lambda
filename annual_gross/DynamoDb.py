import uuid

import boto3

dynamodb = boto3.client('dynamodb')
description = 'Annual gross'
table_name = 'annual_gross'



def save_data(self):
    dynamodb.put_item(TableName=table_name,
    Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(self)},
                                'description': {'S': description}})
