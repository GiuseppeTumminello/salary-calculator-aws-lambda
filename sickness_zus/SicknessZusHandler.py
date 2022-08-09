import json

import SicknessZusCalculator
import DynamoDb
import Sqs

DESCRIPTION = 'Sickness zus'


def sickness_zus_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    sickness_zus = SicknessZusCalculator.calculate_health(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: sickness_zus}))
    DynamoDb.save_data(sickness_zus)
    return json.dumps({DESCRIPTION: sickness_zus})