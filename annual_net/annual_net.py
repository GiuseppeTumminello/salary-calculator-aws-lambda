import uuid
import boto3

dynamodb = boto3.client('dynamodb', profile_name="Sandbox_Full-Administrator")
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


def calculate_annual_net(monthly_gross):
    health = calculate_health(monthly_gross)
    if monthly_gross * month < annual_threshold:
        return health - (health * tax_rate_17) * month
    else:
        return health - (health * tax_rate_32) * month


def annual_net_handler(event, context):
    annual_net = calculate_annual_net(event['amount'])
    dynamodb.put_item(TableName='annual_net',
                      Item={'id': {'S': str(uuid.uuid4())}, 'amount': {'N': annual_net},
                            'description': {'S': 'Annual net'}})
    return {'Annual net': "{:10.2f}".format(annual_net)}