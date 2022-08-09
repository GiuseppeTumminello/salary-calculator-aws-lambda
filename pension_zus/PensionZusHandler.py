import json

import PensionZusCalculator
import DynamoDb
import Sqs

DESCRIPTION = 'Pension zus'


def pension_zus_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    pension_zus = PensionZusCalculator.calculate_health(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: pension_zus}))
    DynamoDb.save_data(pension_zus)
    return json.dumps({DESCRIPTION: pension_zus})
