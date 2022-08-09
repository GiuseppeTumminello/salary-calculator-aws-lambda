
import boto3

dynamodb = boto3.client('dynamodb')
DISABILITY_ZUS_RATE = 0.0150
DESCRIPTION = 'Annual net'


def calculate_disability_zus(monthly_gross):
    return monthly_gross * DISABILITY_ZUS_RATE
