import uuid
import boto3

DYNAMODB = boto3.client('dynamodb')
DESCRIPTION = 'Sickness zus'
TABLE_NAME = 'microservices_data'


def save_data(sickness_zus, uuid_from_sqs, description):
    DYNAMODB.put_item(TableName=TABLE_NAME,
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': str(sickness_zus)},
                            'description': {'S': str(description)}, 'uuid': {'S': str(uuid_from_sqs)}})
