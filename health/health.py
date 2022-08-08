import uuid
import boto3

dynamodb = boto3.client('dynamodb')
total_zus_rate = 0.1371
health_rate = 0.09


def calculate_health(monthly_gross):
    return (monthly_gross - (monthly_gross * total_zus_rate)) * 0.09


def health_handler(event, context):
    health = calculate_health(event['amount'])
    dynamodb.put_item(TableName='health',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': health},
                            'description': {'S': 'Health'}})
    return {'Health': "{:10.2f}".format(health)}
