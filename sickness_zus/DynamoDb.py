import uuid
import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Sickness zus'
TABLE_NAME = 'sickness-zus'


def save_data(sickness_zus):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(sickness_zus)},
                            'description': {'S': DESCRIPTION}})
