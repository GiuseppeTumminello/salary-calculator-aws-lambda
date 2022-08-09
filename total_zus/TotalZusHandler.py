import json

import TotalZusCalculator
import DynamoDb
import Sqs

DESCRIPTION = 'Sickness zus'


def pension_zus_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    total_zus = TotalZusCalculator.calculate_health(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: total_zus}))
    DynamoDb.save_data(total_zus)
    return json.dumps({DESCRIPTION: total_zus})
