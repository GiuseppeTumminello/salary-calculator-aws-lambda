import uuid
import boto3

dynamodb = boto3.client('dynamodb')
total_zus_rate = 0.1371
health_rate = 0.09
annual_threshold = 120000
tax_rate_17 = 0.0832
tax_rate_32 = 0.1432
month = 12


def calculate_total_zus(monthly_gross):
    return monthly_gross - monthly_gross * total_zus_rate


def calculate_health(monthly_gross):
    return calculate_total_zus(monthly_gross) - (calculate_total_zus(monthly_gross) * health_rate)


def calculate_tax(monthly_gross):
    health = calculate_health(monthly_gross)
    if monthly_gross * month < annual_threshold:
        return health * tax_rate_17
    else:
        return health * tax_rate_32


def tax_handler(event, context):
    tax = calculate_tax(event['amount'])
    dynamodb.put_item(TableName='tax',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': tax},
                            'description': {'S': 'Tax'}})
    return {'Tax': "{:10.2f}".format(tax)}
