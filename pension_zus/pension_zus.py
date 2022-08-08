import uuid
import boto3

dynamodb = boto3.client('dynamodb')
pension_zus_rate = 0.0976


def calculate_pension_zus(monthly_gross):
    return monthly_gross * pension_zus_rate


def pension_zus_handler(event, context):
    pension_zus = calculate_pension_zus(event['amount'])
    dynamodb.put_item(TableName='pension_zus',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': pension_zus},
                            'description': {'S': 'Pension zus'}})
    return {'Pension zus': "{:10.2f}".format(pension_zus)}
