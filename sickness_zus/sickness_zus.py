import uuid
import boto3

dynamodb = boto3.client('dynamodb')
sickness_zus_rate = 0.0245


def calculate_sickness_zus(monthly_gross):
    return monthly_gross * sickness_zus_rate


def sickness_zus_handler(event, context):
    sickness_zus = calculate_sickness_zus(event['amount'])
    dynamodb.put_item(TableName='sickness_zus',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': sickness_zus},
                            'description': {'S': 'Sickness zus'}})
    return {'Sickness zus': "{:10.2f}".format(sickness_zus)}