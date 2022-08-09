import uuid
import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Monthly net'
TABLE_NAME = 'monthly-net'


def save_data(monthly_net):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(monthly_net)},
                            'description': {'S': DESCRIPTION}})
