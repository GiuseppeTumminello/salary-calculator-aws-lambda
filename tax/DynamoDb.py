import uuid
import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Tax '
TABLE_NAME = 'tax'


def save_data(tax):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(tax)},
                            'description': {'S': DESCRIPTION}})
