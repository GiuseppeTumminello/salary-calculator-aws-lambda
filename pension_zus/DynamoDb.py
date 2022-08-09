import uuid
import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Pension zus'
TABLE_NAME = 'pension_zus'


def save_data(pension_zus):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(pension_zus)},
                            'description': {'S': DESCRIPTION}})
