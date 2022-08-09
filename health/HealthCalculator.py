import boto3

DYNAMODB = boto3.client('dynamodb')
TOTAL_ZUS_RATE = 0.1371
HEALTH_RATE = 0.09


def calculate_health(monthly_gross):
    return (monthly_gross - (monthly_gross * TOTAL_ZUS_RATE)) * 0.09
