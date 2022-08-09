import json

import MonthlyNetCalculator
import DynamoDb
import Sqs

DESCRIPTION = 'Monthly net'


def pension_zus_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    monthly_net = MonthlyNetCalculator.calculate_health(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: monthly_net}))
    DynamoDb.save_data(monthly_net)
    return json.dumps({DESCRIPTION: monthly_net})

