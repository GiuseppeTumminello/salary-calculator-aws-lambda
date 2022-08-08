import uuid
import boto3

dynamodb = boto3.client('dynamodb')
disability_zus_rate = 0.0150


def calculate_disability_zus(monthly_gross):
    return monthly_gross * disability_zus_rate


def disability_zus_handler(event, context):
    disability_zus = calculate_disability_zus(event['amount'])
    dynamodb.put_item(TableName='disability_zus',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': disability_zus},
                            'description': {'S': 'Disability zus'}})
    return {'Disability zus': "{:10.2f}".format(disability_zus)}