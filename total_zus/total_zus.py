import uuid
import boto3

dynamodb = boto3.client('dynamodb')
total_zus_rate = 0.1371


def calculate_total_zus(monthly_gross):
    return monthly_gross * total_zus_rate


def total_zus_handler(event, context):
    total_zus = calculate_total_zus(event['amount'])
    dynamodb.put_item(TableName='total_zus',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': total_zus},
                            'description': {'S': 'Total zus'}})
    return {'Total zus': "{:10.2f}".format(total_zus)}
